from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task

# add task (teacher)
@api_view(['POST'])
def add_task(request):
    title = request.data.get("title")
    description = request.data.get("description")
    subject = request.data.get("subject")
    due_date = request.data.get("due_date")

    Task.objects.create(
        title=title,
        description=description,
        subject=subject,
        due_date=due_date
    )

    return Response({"message":"Task added"})


# student view tasks
@api_view(['GET'])
def view_tasks(request):
    tasks = Task.objects.all().values()
    return Response(tasks)
