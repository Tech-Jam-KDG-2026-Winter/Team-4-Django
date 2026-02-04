from django.shortcuts import render
from django.views import View

from .services import send_test_email


class EmailTestView(View):
    template_name = "reflections/test_email.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        to_email = request.POST.get("email")
        success, error_message = send_test_email(to_email)

        context = {
            "to_email": to_email,
            "success": success,
            "error_message": error_message,
        }
        return render(request, self.template_name, context)


class VoiceInputTestView(View):
    """Web Speech API による音声入力（音声→テキスト）のテスト用ビュー。"""

    template_name = "reflections/voice_input_test.html"

    def get(self, request):
        return render(request, self.template_name)


