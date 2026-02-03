from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from apps.users import views as user_views

def root(request):
    return JsonResponse({"service": "Drift Jellyfish", "status": "ok"})

urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("login/", user_views.login_page, name="login-page"),
    path("api/users/", include('apps.users.urls')),
    path('api/tasks/', include('apps.tasks.urls')),
]