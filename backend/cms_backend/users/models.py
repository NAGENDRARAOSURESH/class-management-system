from django.db import models

# ================= USER =================
     
class User(models.Model):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    gender = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    student_class = models.CharField(max_length=20, blank=True, null=True)
    task_completed = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# ================= CHAT =================
class Message(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


# ================= TASK =================
class Task(models.Model):
    student_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    due_date = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# ================= ATTENDANCE =================
class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name
