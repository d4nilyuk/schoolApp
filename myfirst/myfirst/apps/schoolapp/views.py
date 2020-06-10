from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Student, Teacher, Lesson
from django.template.response import TemplateResponse

def home(request):
    return TemplateResponse(request, 'home.html', {'redirect_url': 'home.html'})

def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('schoolapp:home')
    else:
        form = UserCreationForm()
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
        student = Student.objects.order_by('last_name')
    except:
        raise Http404("No students are found")

    return render(request, 'students/students.html', {'student': student})

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

def student_details(request, student_id):
    try:
        a = Student.objects.get(id = student_id)
    except:
        raise Http404("Student is not found")
    
    return render(request, 'students/students.html', {'student': a}) 

def teacher_details(request, teacher_id):
    try:
        a = Teacher.objects.get(id = teacher_id)
    except:
        raise Http404("Teacher is not found")
    
    return render(request, 'teachers/teachers.html', {'teacher': a}) 

def lesson_details(request, lesson_id):
    try:
        a = Lesson.objects.get(id = lesson_id)
    except:                 
        raise Http404("Lesson is not found")
    
    return render(request, 'lessons/lessons.html', {'lesson': a}) 




