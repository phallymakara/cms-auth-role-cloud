from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomUserCreationForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ──► role-based redirect block (belongs right here)
            if user.role == 'student':
                return redirect('student-dashboard')
            elif user.role == 'instructor':
                return redirect('instructor-dashboard')
            elif user.role == 'admin':
                return redirect('admin-dashboard')
            else:
                return redirect('home')   # fallback
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def student_dashboard(request):
    return HttpResponse("<h1>Welcome, Student!</h1>")


@login_required
def instructor_dashboard(request):
    return HttpResponse("<h1>Welcome, Instructor!</h1>")


@login_required
def admin_dashboard(request):
    return HttpResponse("<h1>Welcome, Admin!</h1>")
