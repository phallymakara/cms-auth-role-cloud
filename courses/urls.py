from django.urls import path
from .views import create_course
from django.urls import path
from .views import create_course, course_list, enroll_in_course

urlpatterns = [
    path('create/', create_course, name='create-course'),
    path('list/', course_list, name='course-list'),
    path('enroll/<int:course_id>/', enroll_in_course, name='enroll'),
]
