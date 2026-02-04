from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import date
from .models import DailyReflection
from .services import send_test_email


# テスト用ビュー
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


# 振り返りAPI
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_reflection(request):
    """振り返り作成（チェックボックス用）"""
    user = request.user
    today = date.today()
    
    # 既存の振り返りを取得または作成
    reflection, created = DailyReflection.objects.get_or_create(
        user=user,
        date=today,
        defaults={
            'hello_count': 0,
            'thanks_given': False,
            'thanks_received': False
        }
    )
    
    # リクエストデータから更新
    if 'hello_count' in request.data:
        reflection.hello_count = request.data['hello_count']
    if 'thanks_given' in request.data:
        reflection.thanks_given = request.data['thanks_given']
    if 'thanks_received' in request.data:
        reflection.thanks_received = request.data['thanks_received']
    
    reflection.save()
    
    return Response(
        {
            "message": "振り返りを保存しました",
            "reflection_id": reflection.reflection_id
        },
        status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_reflection(request):
    """振り返り更新（テキスト入力用）"""
    user = request.user
    today = date.today()
    
    try:
        reflection = DailyReflection.objects.get(user=user, date=today)
    except DailyReflection.DoesNotExist:
        return Response(
            {"error": "振り返りが見つかりません。先にチェックボックス画面で振り返りを作成してください。"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # テキストを更新
    if 'good_thing' in request.data:
        reflection.good_thing = request.data['good_thing']
    if 'bad_thing' in request.data:
        reflection.bad_thing = request.data['bad_thing']
    
    reflection.save()
    
    return Response(
        {
            "message": "振り返りを更新しました",
            "reflection_id": reflection.reflection_id
        },
        status=status.HTTP_200_OK
    )


# HTML表示用ビュー
@login_required
def review_1_page(request):
    """振り返りチェックボックス画面"""
    return render(request, "review-1.html")


@login_required
def review_2_page(request):
    """振り返りテキスト入力画面"""
    return render(request, "review-2.html")


class ReflectionListView(TemplateView):
    template_name = "reflections/list.html"