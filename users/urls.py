from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    student_dashboard, instructor_dashboard, admin_dashboard
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    # ✅ Dashboard URLs
    path('dashboard/student/', student_dashboard, name='student-dashboard'),
    path('dashboard/instructor/', instructor_dashboard, name='instructor-dashboard'),
    path('dashboard/admin/', admin_dashboard, name='admin-dashboard'),
]
