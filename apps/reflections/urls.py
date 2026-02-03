from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_reflection, name='create-reflection'),
    path('update/', views.update_reflection, name='update-reflection'),
]
