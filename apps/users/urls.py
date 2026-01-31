from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('me/', views.get_current_user, name='current-user'),
    path('me/mode/', views.select_mode, name='select-mode'),
]
