from django.contrib import admin

# Register your models here.

from .models import Lesson, Teacher, Student

admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Student)