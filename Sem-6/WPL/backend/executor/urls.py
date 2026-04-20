from django.urls import path
from . import views

urlpatterns = [
    path('execute/', views.execute_code, name='execute_code'),
    path('ast/', views.generate_ast, name='generate_ast'),
    path('history/', views.execution_history, name='execution_history'),
    path('health/', views.health_check, name='health_check'),
]
