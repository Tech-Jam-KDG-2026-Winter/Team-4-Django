from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
# from apps.common.api.health import healthz
from apps.users import views as user_views
from apps.tasks import views as task_views
from apps.reflections import views as reflection_views
from apps.tasks import views as task_views


def root(request):
    return JsonResponse({"service": "Drift Jellyfish", "status": "ok"})


urlpatterns = [
    path("", root),
    path("admin/", admin.site.urls),
    
    # ヘルスチェック
    # path("healthz/", healthz),
    
    # 認証画面
    path("login/", user_views.login_page, name="login-page"),
    path("signup/", user_views.signup_page, name="signup-page"),
    path("profile/", user_views.profile_page, name='profile-page'),
    
    # モード選択
    path("mode-question/", user_views.mode_question_page, name="mode-question"),
    path("mode-restart/", user_views.mode_restart_page, name="mode-restart"),
    path("mode-maintainimprove/", user_views.mode_maintainimprove_page, name="mode-maintainimprove"),

    path("target/", task_views.target_page, name="target"),
    
    # タスク画面
    path("task-today/", task_views.task_today_page, name="task-today"),
    path("task-clear/", task_views.task_clear_page, name="task-clear"),
    
    # 待機画面
    path("waiting/", user_views.waiting_page, name='waiting-page'),
    path("waiting-before-reflection/", user_views.waiting_before_reflection_page, name="waiting-before-reflection"),
    
    # 振り返り画面
    path("review-1/", reflection_views.review_1_page, name='review-1'),
    path("review-2/", reflection_views.review_2_page, name='review-2'),
    
    # API
    path("api/users/", include("apps.users.urls")),
    path("api/tasks/", include("apps.tasks.urls")),
    path("api/reflections/", include("apps.reflections.urls")),
    
    # テスト用（開発中）
    path("reflections/", include("apps.reflections.urls")),
]