from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Attendance

# teacher mark attendance
@api_view(['POST'])
def mark_attendance(request):
    name = request.data.get("student_name")
    date = request.data.get("date")
    status = request.data.get("status")

    Attendance.objects.create(
        student_name=name,
        date=date,
        status=status
    )

    return Response({"message":"Attendance marked"})


# student view attendance
@api_view(['GET'])
def view_attendance(request):
    data = Attendance.objects.all().values()
    return Response(data)
