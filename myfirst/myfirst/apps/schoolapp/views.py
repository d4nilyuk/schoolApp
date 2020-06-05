from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from.models import Student, Teacher, SchoolClass

def students(request):
    student = Student.objects.order_by('student_id')
    return render(request, 'students/students.html', {'student': student})

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