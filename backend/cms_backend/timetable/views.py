from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Timetable

# teacher add timetable
@api_view(['POST'])
def add_timetable(request):
    day = request.data.get("day")
    subject = request.data.get("subject")
    time = request.data.get("time")

    Timetable.objects.create(
        day=day,
        subject=subject,
        time=time
    )

    return Response({"message":"Timetable added"})


# student view timetable
@api_view(['GET'])
def view_timetable(request):
    data = Timetable.objects.all().values()
    return Response(data)
