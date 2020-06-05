from django.urls import path

from . import views

app_name = 'schoolapp'
urlpatterns = [
    path('students', views.index, name = 'student'),
    path('students/<int:student_id>/', views.student_details, name = 'student_details')
]
