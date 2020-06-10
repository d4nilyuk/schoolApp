from django.db import models
from django import forms
from enum import unique
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.aggregates import Count, Sum
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save

# Create your models here.

USER_TYPE= [
    ('student', 'Students'),
    ('teacher', 'Teachers'),
    ]
"""
class RegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_TYPE, widget=forms.RadioSelect)
    
    class Meta:
        model = User
        fields = [
            'user_type',
            'username',
            'email'
        ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']

        if commit:
            user.save()

        return user
"""

class Lesson(models.Model):
    lesson_title = models.CharField('Lesson name', max_length = 30)

    def __str__(self):
        return self.lesson_title
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
    first_name = models.CharField('First Name', max_length = 30)
    last_name = models.CharField('Last Name', max_length = 30)
    hourlyRate = models.IntegerField()
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=True)
    
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
    first_name = models.CharField('First Name', max_length = 30)
    last_name = models.CharField('Last Name', max_length = 30)
    lesson = models.ForeignKey(Lesson, on_delete = models.CASCADE)
    is_student = models.BooleanField('student status', default=True)
    is_teacher = models.BooleanField('teacher status', default=False)
    attendence = models.BooleanField()

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

