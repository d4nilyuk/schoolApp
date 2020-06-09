from django.db import models
from django import forms
from enum import unique
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.db.models.aggregates import Count, Sum

# Create your models here.

class SchoolClass(models.Model):
    schoolclass_name = models.CharField('Class name', max_length = 30)
    schoolclass_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.schoolclass_name
    
    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(SchoolClass, on_delete = models.CASCADE)
    teacher_first_name = models.CharField('First Name', max_length = 30)
    teacher_last_name = models.CharField('Last Name', max_length = 30)
    teacher_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hourlyRate = models.IntegerField()
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    @classmethod
    def total_user_spend(cls):
        return cls.objects.aggregate(total='hourlyRate' * Count('lesson'))

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_first_name = models.CharField('First Name', max_length = 30)
    student_last_name = models.CharField('Last Name', max_length = 30)
    schoolClass = models.ForeignKey(SchoolClass, on_delete = models.CASCADE)
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attendence = models.BooleanField()

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

