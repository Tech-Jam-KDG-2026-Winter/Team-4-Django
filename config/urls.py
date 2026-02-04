from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from apps.users import views as user_views
from apps.tasks import views as task_views
from apps.reflections import views as reflection_views
from apps.users.views import ProfileView  # これは削除してもOK
from apps.reflections.views import ReflectionListView

def root(request):
    return JsonResponse({"service": "Drift Jellyfish", "status": "ok"})

urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    path("login/", user_views.login_page, name="login-page"),
    path("signup/", user_views.signup_page, name="signup-page"),  # 修正
    path("profile/", user_views.profile_page, name='profile-page'),  # 修正
    path("list/", ReflectionListView.as_view(), name='list'),
    path("api/users/", include("apps.users.urls")),
    path("api/tasks/", include("apps.tasks.urls")),
    path("task-today/", task_views.task_today_page, name="task-today"),
    path("task-clear/", task_views.task_clear_page, name="task-clear"),
    path("waiting-before-reflection/", user_views.waiting_before_reflection_page, name="waiting-before-reflection"),
    path("api/reflections/", include("apps.reflections.urls")),
    path('waiting/', user_views.waiting_page, name='waiting-page'),
    path("mode-question/", user_views.mode_question_page, name="mode-question"),
    path("mode-restart/", user_views.mode_restart_page, name="mode-restart"),
    path("mode-maintainimprove/", user_views.mode_maintainimprove_page, name="mode-maintainimprove"),
]