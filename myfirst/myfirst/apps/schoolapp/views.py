from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

from.models import Student, Teacher, SchoolClass
from django.template.response import TemplateResponse

def home(request):
    return TemplateResponse(request, 'home.html', {'redirect_url': 'home.html'})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('schoolapp:teacher')
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
        student = Student.objects.order_by('student_id')
    except:
        raise Http404("No students are found")
    return render(request, 'students/students.html', {'student': student})

def teachers(request):
    try:
        teacher = Teacher.objects.order_by('teacher_id')
    except:
        raise Http404("No teachers are found")
    return render(request, 'teachers/teachers.html', {'teacher': teacher})

def schoolclasses(request):
    try:
        schoolclass = SchoolClass.objects.order_by('schoolclass_id')
    except:
        raise Http404("No classes are found")
    return render(request, 'schoolclasses/schoolclasses.html', {'schoolclass': schoolclass})

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

def schoolclass_details(request, schoolclass_id):
    try:
        a = SchoolClass.objects.get(id = schoolclass_id)
    except:
        raise Http404("Class is not found")
    
    return render(request, 'schoolclasses/schoolclasses.html', {'schoolclass': a}) 

def salary(request, teacher_id):
    try:
        a = Teacher.total_user_spend(id = teacher_id)
    except:
        raise Http404("No Payments is found")

    return render(request, 'teachers/payments.html', {'payment': a}) 


