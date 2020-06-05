from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from.models import Student, Teacher, SchoolClass

def index(request):
    student = Student.objects.order_by('student_id')
    return render(request, 'students/students.html', {'student': student})

def student_details(request, student_id):
    try:
        a = Student.objects.get(id = student_id)
    except:
        raise Http404("Student is not found")
    
    return render(request, 'students/students.html', {'student': a}) 