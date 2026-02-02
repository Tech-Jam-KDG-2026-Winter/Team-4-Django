from django.urls import path
from . import views

urlpatterns = [
    path('today/', views.get_today_task, name='get-today-task'),
    path('<int:task_id>/complete/', views.complete_task, name='complete-task'),
    path('<int:task_id>/change/', views.change_task, name='change-task'),
]
