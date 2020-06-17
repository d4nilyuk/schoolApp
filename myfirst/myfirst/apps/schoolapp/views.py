from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Student, Teacher, Lesson, RegistrationForm
from django.template.response import TemplateResponse
from django.db.models import Avg, Count

def home(request):
    return TemplateResponse(request, 'home.html', {'redirect_url': 'home.html'})

def add_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('schoolapp:home')
    else:
        form = RegistrationForm()
    return render(request, 'add_user.html', {'form': form})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('schoolapp:home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        login(request)
        return redirect('schoolapp:home')
    return render(request, 'home.html', {'redirect_url': 'home.html'})

def students(request):
    try:
        a = Student.objects.order_by('last_name')
    except:
        raise Http404("No students are found")

    return render(request, 'students/students.html', {'student': a})

def teachers(request):
    try:
        teacher = Teacher.objects.order_by('last_name')
    except:
        raise Http404("No teachers are found")

    return render(request, 'teachers/teachers.html', {'teacher': teacher})

def lessons(request):
    try:
        lesson = Lesson.objects.order_by('lesson_title')
    except:
        raise Http404("No lesson are found")

    return render(request, 'lessons/lessons.html', {'lesson': lesson})

def timetable(request):
    try:
        a = Lesson.objects.order_by('lesson_title')
    except:
        raise Http404("No lesson are found")

    return render(request, 'timetable.html', {'lesson': a})
