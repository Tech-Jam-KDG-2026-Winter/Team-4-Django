from django.urls import path
from . import views
from .views import EmailTestView, VoiceInputTestView

app_name = "reflections"

urlpatterns = [
    # 振り返りAPI
    path('', views.create_reflection, name='create-reflection'),
    path('update/', views.update_reflection, name='update-reflection'),
    
    # テスト用
    path("test-email/", EmailTestView.as_view(), name="test_email"),
    path("voice-input-test/", VoiceInputTestView.as_view(), name="voice_input_test"),
]