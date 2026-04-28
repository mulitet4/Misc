from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('student', views.student, name='student'),
  path('subject', views.subject_form, name='subject'),
  path('car', views.car_form, name='car_form'),
  path('car_result', views.car_result, name='car_result'),
]