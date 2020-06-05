from django.urls import path

from . import views
from django.conf.urls import url

app_name = 'schoolapp'
urlpatterns = [
    path('', views.home, name = 'Home'),

    url(r'^login/$', views.login, name='login'),
    #url(r'^logout/$', views.logout, name='logout'),

    path('students', views.students, name = 'student'),
    path('students/<int:student_id>/', views.student_details, name = 'student_details'),

    path('teachers', views.teachers, name = 'teacher'),
    path('teachers/<int:teacher_id>/', views.teacher_details, name = 'teacher_details'),

    path('schoolclasses', views.schoolclasses, name = 'schoolclass'),
    path('schoolclasses/<int:schoolclass_id>/', views.schoolclass_details, name = 'schoolclass_details')
]
