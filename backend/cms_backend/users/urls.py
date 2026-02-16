from django.urls import path
from .views import login_view, signup_view, send_message, get_messages, delete_message, get_students, student_attendance, student_tasks, dashboard_counts, get_profile,update_profile


urlpatterns = [
    path('login/', login_view),
    path('signup/', signup_view),

    # chat
    path('send-message/', send_message),
    path('get-messages/', get_messages),
    path('delete-message/<int:id>/', delete_message),

    # students list
    path('students/', get_students),
    
    path('student-tasks/<str:name>/', student_tasks),
path('student-attendance/<str:name>/', student_attendance),
path('dashboard-counts/', dashboard_counts),
path('profile/<str:name>/', get_profile),
path('update-profile/', update_profile),


]
