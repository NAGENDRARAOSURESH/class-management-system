from django.urls import path
from .views import add_timetable, view_timetable

urlpatterns = [
    path('add-timetable/', add_timetable),
    path('view-timetable/', view_timetable),
]
