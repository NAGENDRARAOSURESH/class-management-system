from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User, Message, Task, Attendance


# ================= LOGIN =================
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"error": "Email and password required"})

    user = User.objects.filter(email=email, password=password).first()

    if user:
        return Response({
            "message": "Login success",
            "role": user.role,
            "user_id": user.id,
            "name": user.name
        })
    else:
        return Response({"error": "Invalid login"})


# ================= SIGNUP =================
@api_view(['POST'])
def signup_view(request):
    name = request.data.get("name")
    email = request.data.get("email")
    password = request.data.get("password")
    role = request.data.get("role")

    if not name or not email or not password or not role:
        return Response({"error": "All fields required"})

    if User.objects.filter(email=email).exists():
        return Response({"error": "Email already exists"})

    User.objects.create(
        name=name,
        email=email,
        password=password,
        role=role
    )

    return Response({"message": "Account created successfully"})


# ================= CHAT SEND =================
@api_view(['POST'])
def send_message(request):
    sender = request.data.get("sender")
    receiver = request.data.get("receiver")
    message = request.data.get("message")

    if not sender or not message:
        return Response({"error": "Message empty"})

    Message.objects.create(
        sender=sender,
        receiver=receiver,
        message=message
    )

    return Response({"message": "Message sent"})


# ================= GET CHAT =================
@api_view(['GET'])
def get_messages(request):
    data = Message.objects.all().order_by("id").values()
    return Response(data)


# ================= DELETE CHAT =================
@api_view(['DELETE'])
def delete_message(request, id):
    msg = get_object_or_404(Message, id=id)
    msg.delete()
    return Response({"message": "Deleted successfully"})


# ================= GET ALL STUDENTS =================
@api_view(['GET'])
def get_students(request):
    students = User.objects.filter(role="student").values()
    return Response(students)


# ================= SINGLE STUDENT TASKS =================
@api_view(['GET'])
def student_tasks(request, name):
    data = Task.objects.filter(student_name=name).values()
    return Response(data)


# ================= SINGLE STUDENT ATTENDANCE =================
@api_view(['GET'])
def student_attendance(request, name):
    data = Attendance.objects.filter(student_name=name).values()
    return Response(data)


# ================= DASHBOARD COUNTS (REAL DATA) =================
@api_view(['GET'])
def dashboard_counts(request):

    total_students = User.objects.filter(role="student").count()
    total_tasks = Task.objects.count()

    present = Attendance.objects.filter(status="Present").count()
    total = Attendance.objects.count()

    percent = 0
    if total > 0:
        percent = int((present / total) * 100)

    return Response({
        "students": total_students,
        "tasks": total_tasks,
        "attendance": percent
    })
# ===== GET PROFILE =====
@api_view(['GET'])
def get_profile(request, name):
    try:
        user = User.objects.get(name=name)
        return Response({
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "gender": user.gender,
            "mobile": user.mobile,
            "class": user.student_class,
            "task_completed": user.task_completed
        })
    except:
        return Response({"error":"User not found"})

# ===== UPDATE PROFILE =====
@api_view(['POST'])
def update_profile(request):
    name = request.data.get("name")

    user = User.objects.get(name=name)

    user.gender = request.data.get("gender")
    user.mobile = request.data.get("mobile")
    user.student_class = request.data.get("student_class")
    user.task_completed = request.data.get("task_completed",0)
    user.save()

    return Response({"message":"Profile updated"})

