from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

def root(request):
    return JsonResponse({"service": "Drift Jellyfish", "status": "ok"})

urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("api/users/", include('apps.users.urls')),
]