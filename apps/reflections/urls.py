from django.urls import path

from .views import EmailTestView, VoiceInputTestView

app_name = "reflections"

urlpatterns = [
    path("test-email/", EmailTestView.as_view(), name="test_email"),
    path("voice-input-test/", VoiceInputTestView.as_view(), name="voice_input_test"),
]


