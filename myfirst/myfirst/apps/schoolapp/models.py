from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField('Teacher First name', max_length = 100)
    last_name = models.CharField('Teacher Last name', max_length = 100)
    hourlyRate = models.IntegerField()

    def __str__(self):
        return self.last_name

class SchoolClass(models.Model):
    class_id = models.IntegerField()

    def __str__(self):
        return self.class_id

class Student(models.Model):
    schoolClass = models.ForeignKey(SchoolClass, on_delete = models.CASCADE)
    first_name = models.CharField('Student First name', max_length = 100)
    last_name = models.CharField('Student Last name', max_length = 100)
    enrolNum = models.IntegerField()
    details = models.TextField('Student Details')
    attendence = models.BooleanField()

    def __str__(self):
        return self.schoolClass

