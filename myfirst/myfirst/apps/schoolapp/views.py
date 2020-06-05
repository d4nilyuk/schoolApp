from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render


from.models import Student, Teacher, SchoolClass

def teacher(request, teacher_id):
    teachers_list = Teacher.objects.order_by('last_name')
    return render(request, 'content/teachers.html'), {'teachers_list': teachers_list}

def student(request, student_id):
    students_list = Teacher.objects.order_by('last_name')
    return render(request, 'content/students.html'), {'students_list': students_list}

def schoolclass(request, schoolclass_id):
    schoolclasses_list = Teacher.objects.order_by('class_id')
    return render(request, 'content/schoolclass.html'), {'schoolclasses_list': schoolclasses_list}

