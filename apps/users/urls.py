from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('me/', views.get_current_user, name='current-user'),
    path('me/mode/', views.select_mode, name='select-mode'),
    path('me/time/', views.update_time_settings, name='update-time-settings'),
    path('me/profile/', views.get_profile, name='get-profile'),
    path('me/account/', views.update_account, name='update-account'),
    path('complete/', views.complete_page, name='complete-page'),
    path('waiting/', views.waiting_page, name='waiting-page'),
    path('waiting-before-reflection/', views.waiting_before_reflection_page, name='waiting-before-reflection-page'),
]
