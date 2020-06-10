from django.urls import path

from . import views
from django.conf.urls import url
from django.views.generic import TemplateView

app_name = 'schoolapp'
urlpatterns = [
    path('home', views.home, name = 'home'),
    path('', views.home, name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    path('add_user', views.add_user, name = 'add_user'),
    path('students', views.students, name = 'student'),
    path('teachers', views.teachers, name = 'teacher'),
    path('lessons', views.lessons, name = 'lesson'),
    path('timetable', views.timetable, name = 'timetable')
]
