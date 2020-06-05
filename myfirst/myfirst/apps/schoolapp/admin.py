from django.contrib import admin

# Register your models here.

from .models import SchoolClass, Teacher, Student

admin.site.register(SchoolClass)
admin.site.register(Teacher)
admin.site.register(Student)