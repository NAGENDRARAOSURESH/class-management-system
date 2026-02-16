from django.urls import path
from .views import add_task, view_tasks

urlpatterns = [
    path('add-task/', add_task),
    path('view-tasks/', view_tasks),
]
