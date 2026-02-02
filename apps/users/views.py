from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token  # ← 追加
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, LoginSerializer, UserSerializer,TimeSettingsSerializer,ModeSelectionSerializer  # LoginSerializerに変更


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """ユーザー登録"""
    serializer = UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # 登録時にトークンも作成
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "message": "ユーザー登録が完了しました",
                "token": token.key,
                "user": UserSerializer(user).data
            },
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    """ログイン（トークン認証）"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        
        # トークンを取得または作成
        token, created = Token.objects.get_or_create(user=user)
        
        return Response(
            {
                "message": "ログインしました",
                "token": token.key,
                "user": UserSerializer(user).data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    """ログアウト（トークン削除）"""
    # ユーザーのトークンを削除
    request.user.auth_token.delete()
    return Response(
        {"message": "ログアウトしました"},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    """現在のユーザー情報取得"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def select_mode(request):
    """モード選択"""
    user = request.user
    
    # すでにモード選択済みの場合
    if user.mode is not None:
        return Response(
            {"error": "モードは既に選択されています"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    serializer = ModeSelectionSerializer(data=request.data)
    if serializer.is_valid():
        selected_mode = serializer.validated_data['mode']
        user.mode = selected_mode
        
        # 維持モードの場合、challenge_day を 8 に設定
        if selected_mode == 'keep':
            user.challenge_day = 8
        # 再始動モードの場合、challenge_day は 1 のまま（デフォルト）
        
        user.save()
        
        return Response(
            {
                "message": "モードを設定しました",
                "user": UserSerializer(user).data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_time_settings(request):
    """タスク・振り返り時刻の設定"""
    user = request.user
    serializer = TimeSettingsSerializer(data=request.data)
    
    if serializer.is_valid():
        # 指定された時刻のみ更新
        if 'task_time' in serializer.validated_data:
            user.task_time = serializer.validated_data['task_time']
        
        if 'reflection_time' in serializer.validated_data:
            user.reflection_time = serializer.validated_data['reflection_time']
        
        user.save()
        
        return Response(
            {
                "message": "時刻設定を更新しました",
                "user": UserSerializer(user).data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)