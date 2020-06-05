from django.db import models
from enum import unique

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField('Teacher First name', max_length = 30)
    last_name = models.CharField('Teacher Last name', max_length = 30)
    teacher_id = models.IntegerField(unique=True)
    hourlyRate = models.IntegerField()

    def __str__(self):
        return self.last_name
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

class SchoolClass(models.Model):
    schoolclass_name = models.CharField('Class name', max_length = 30)
    schoolclass_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.schoolclass_name
    
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'


class Student(models.Model):
    schoolClass = models.ForeignKey(SchoolClass, on_delete = models.CASCADE)
    first_name = models.CharField('Student First name', max_length = 30)
    last_name = models.CharField('Student Last name', max_length = 30)
    enrolNum = models.IntegerField()
    details = models.TextField('Student Details')
    attendence = models.BooleanField()
    student_id = models.IntegerField(unique=True)

    def __str__(self):
        return self.last_name
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

