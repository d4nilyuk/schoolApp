from django.urls import path

from . import views

urlpatterns = [
    path('<int:teacher_id>/', views.teacher, name = 'teacher'),
    path('<int:student_id>/', views.student, name = 'student'),
    path('<int:schoolclass_id>/', views.schoolclass, name = 'schoolclass')

]
