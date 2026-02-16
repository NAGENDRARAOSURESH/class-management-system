from django.urls import path
from .views import mark_attendance, view_attendance

urlpatterns = [
    path('mark-attendance/', mark_attendance),
    path('view-attendance/', view_attendance),
]
