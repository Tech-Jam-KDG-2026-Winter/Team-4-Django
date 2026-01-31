from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token  # ← 追加
from django.contrib.auth import authenticate
from .serializers import UserRegisterSerializer, LoginSerializer, UserSerializer,ModeSelectionSerializer  # LoginSerializerに変更


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
        user.mode = serializer.validated_data['mode']
        user.save()
        
        return Response(
            {
                "message": "モードを設定しました",
                "user": UserSerializer(user).data
            },
            status=status.HTTP_200_OK
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)