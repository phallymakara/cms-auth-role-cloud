from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from .models import Course
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Enrollment
from users.models import CustomUser

@login_required
def create_course(request):
    if request.user.role != 'instructor':
        return redirect('home')  # block non-instructors

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('instructor-dashboard')
    else:
        form = CourseForm()

    return render(request, 'courses/create_course.html', {'form': form})

@login_required
def course_list(request):
    if request.user.role != 'student':
        return redirect('home')  # Only students can view

    enrolled_courses = Enrollment.objects.filter(student=request.user).values_list('course_id', flat=True)
    courses = Course.objects.exclude(id__in=enrolled_courses)

    return render(request, 'courses/course_list.html', {'courses': courses})

@login_required
def enroll_in_course(request, course_id):
    if request.user.role != 'student':
        return redirect('home')

    course = get_object_or_404(Course, id=course_id)

    # prevent duplicate enrollment
    Enrollment.objects.get_or_create(student=request.user, course=course)

    return redirect('course-list')

