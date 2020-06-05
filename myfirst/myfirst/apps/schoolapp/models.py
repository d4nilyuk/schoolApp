from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField('Teacher First name', max_length = 100)
    last_name = models.CharField('Teacher Last name', max_length = 100)
    hourlyRate = models.IntegerField

class schoolClass(models.Model):
    class_id = models.IntegerField

class Student(models.Model):
    schoolClass = models.ForeignKey(schoolClass, on_delete = models.CASCADE)
    first_name = models.CharField('Student First name', max_length = 100)
    last_name = models.CharField('Student Last name', max_length = 100)
    enrolNum = models.IntegerField
    details = models.TextField('Student Details')
    attendence = models.BooleanField

