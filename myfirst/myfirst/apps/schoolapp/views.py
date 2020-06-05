from django.http import HttpResponseRedirect, Http404
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

from.models import Student, Teacher, SchoolClass
from django.template.response import TemplateResponse

def home(request):
    return TemplateResponse(request, 'base.html', {'redirect_url': 'base.html'})

def students(request):
    student = Student.objects.order_by('student_id')
    return render(request, 'students/students.html', {'student': student})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('schoolapp:teacher')
    else:
        form = AuthenticationForm()
    return render(request, 'teachers/login.html', {'form': form})

def teachers(request):
    teacher = Teacher.objects.order_by('teacher_id')
    return render(request, 'teachers/teachers.html', {'teacher': teacher})
    
def schoolclasses(request):
    schoolclass = SchoolClass.objects.order_by('schoolclass_id')
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