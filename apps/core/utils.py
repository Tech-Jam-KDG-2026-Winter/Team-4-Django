from functools import wraps
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()


def token_login_required(view_func):
    """
    Token認証をチェックするデコレータ
    Authorizationヘッダーまたはクエリパラメータからトークンを取得
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Authorizationヘッダーからトークンを取得
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        token_key = None
        
        if auth_header.startswith('Token '):
            token_key = auth_header.split(' ')[1]
        else:
            # クエリパラメータからトークンを取得（フォールバック）
            token_key = request.GET.get('token')
        
        if not token_key:
            # トークンがない場合はログインページにリダイレクト
            from django.shortcuts import redirect
            return redirect('/login/')
        
        try:
            token = Token.objects.get(key=token_key)
            request.user = token.user
        except Token.DoesNotExist:
            from django.shortcuts import redirect
            return redirect('/login/')
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view
