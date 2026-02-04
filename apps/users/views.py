from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.tasks.models import DailyTask
from datetime import datetime, timedelta
from .serializers import UserRegisterSerializer, LoginSerializer, UserSerializer,TimeSettingsSerializer,ModeSelectionSerializer,AccountUpdateSerializer
from django.views.generic import TemplateView


def signup_page(request):
    """新規登録画面のHTMLを返すビュー"""
    return render(request, "signup.html")

@login_required
def profile_page(request):
    """プロフィール画面"""
    user = request.user
    
    # 完了タスク数をカウント
    from apps.tasks.models import DailyTask
    completed_tasks = DailyTask.objects.filter(
        user=user,
        is_completed=True
    ).count()
    
    context = {
        'user': user,
        'completed_tasks': completed_tasks
    }
    
    return render(request, 'users/profile.html', context)

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


def login_page(request):
    """ログイン画面（GET: 画面表示、POST: ログイン処理）"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(f"DEBUG: username={username}, password={password}")  # デバッグ用
        
        from django.contrib.auth import login, authenticate
        user = authenticate(username=username, password=password)
        
        print(f"DEBUG: user={user}")  # デバッグ用
        
        if user:
            login(request, user)
            print("DEBUG: ログイン成功")  # デバッグ用
            print(f"DEBUG: session_key={request.session.session_key}")
            return redirect('/mode-question/')
        else:
            print("DEBUG: ログイン失敗")  # デバッグ用
            return render(request, "login.html", {"error": "ユーザー名またはパスワードが正しくありません"})
    
    return render(request, "login.html")

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
    """モード選択・変更"""
    user = request.user
    
    serializer = ModeSelectionSerializer(data=request.data)
    if serializer.is_valid():
        selected_mode = serializer.validated_data['mode']
        
        # モードが変更される場合のみ challenge_day をリセット
        if user.mode != selected_mode:
            # 維持モードの場合、challenge_day を 8 に設定
            if selected_mode == 'keep':
                user.challenge_day = 8
            # 再始動モードの場合、challenge_day を 1 に設定
            elif selected_mode == 'restart':
                user.challenge_day = 1
        
        user.mode = selected_mode
        user.save()
        
        return Response(
            {
                "message": "モードを設定しました" if user.mode is None else "モードを更新しました",
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    """マイページ用プロフィール情報取得"""
    user = request.user
    
    # 完了タスク数をカウント
    from apps.tasks.models import DailyTask
    completed_tasks_count = DailyTask.objects.filter(
        user=user,
        is_completed=True
    ).count()
    
    return Response(
        {
            "username": user.username,
            "email": user.email,
            "mode": user.mode,
            "challenge_day": user.challenge_day,
            "completed_tasks": completed_tasks_count,
            "created_at": user.created_at,
            "task_time": user.task_time,
            "reflection_time": user.reflection_time
        },
        status=status.HTTP_200_OK
    )

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_account(request):
    """アカウント情報編集"""
    user = request.user
    serializer = AccountUpdateSerializer(data=request.data)
    
    if serializer.is_valid():
        # ユーザー名変更
        if 'username' in serializer.validated_data:
            new_username = serializer.validated_data['username']
            # 既に存在するか確認
            if User.objects.filter(username=new_username).exclude(user_id=user.user_id).exists():
                return Response(
                    {"error": "このユーザー名は既に使用されています"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.username = new_username
        
        # メールアドレス変更
        if 'email' in serializer.validated_data:
            user.email = serializer.validated_data['email']
        
        # パスワード変更
        if 'new_password' in serializer.validated_data:
            current_password = serializer.validated_data['current_password']
            # 現在のパスワードを確認
            if not user.check_password(current_password):
                return Response(
                    {"error": "現在のパスワードが正しくありません"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user.set_password(serializer.validated_data['new_password'])
        
        user.save()
        
        return Response(
            {
                "message": "アカウント情報を更新しました",
                "username": user.username,
                "email": user.email
            },
            status=status.HTTP_200_OK
        )
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# 完走画面・待機画面（追加分）
@login_required
def complete_page(request):
    """50日完走画面"""
    user = request.user
    
    # 完了タスク数をカウント
    completed_tasks = DailyTask.objects.filter(
        user=user,
        is_completed=True
    ).count()
    
    context = {
        'user': user,
        'completed_tasks': completed_tasks
    }
    
    return render(request, 'complete.html', context)


@login_required
def waiting_page(request):
    """待機画面（振り返り完了後）"""
    user = request.user
    
    # タスク時刻をHH:MM形式に変換
    task_time = user.task_time.strftime('%H:%M')
    
    # 次のレベル
    next_level = user.challenge_day
    
    context = {
        'user': user,
        'task_time': task_time,
        'next_level': next_level
    }
    
    return render(request, 'waiting.html', context)


@login_required
def waiting_before_reflection_page(request):
    """待機画面（タスク完了後、振り返り前）"""
    user = request.user
    
    # タスク時刻と振り返り時刻を取得
    task_time = user.task_time
    reflection_time = user.reflection_time
    
    # 今日の日付で時刻を組み合わせてdatetimeオブジェクトを作成
    today = datetime.now().date()
    task_datetime = datetime.combine(today, task_time)
    reflection_datetime = datetime.combine(today, reflection_time)
    
    # 振り返りがタスクより前なら翌日扱い
    if reflection_datetime <= task_datetime:
        reflection_datetime += timedelta(days=1)
    
    # 時間差を計算（時間単位）
    time_diff = (reflection_datetime - task_datetime).total_seconds() / 3600
    
    # 時間差に応じてメッセージを変更
    if time_diff < 3:
        message = "少し休んだら、振り返りをしよう"
    elif time_diff < 6:
        message = "ゆっくり休んでね"
    elif time_diff < 9:
        message = "好きなことをして過ごそう"
    elif time_diff < 12:
        message = "のんびりしておいで"
    else:
        # 12時間以上
        reflection_time_str = reflection_time.strftime('%H:%M')
        message = f"ゆっくり1日を楽しんでね"
    
    context = {
        'user': user,
        'reflection_time': reflection_time.strftime('%H:%M'),
        'message': message
    }
    
    return render(request, 'waiting_before_reflection.html', context)


# モード選択画面（mainから追加分）
@login_required
def mode_question_page(request):
    """モード選択画面"""
    print(f"DEBUG mode_question: user={request.user}, is_authenticated={request.user.is_authenticated}")
    return render(request, "mode-question.html")


@login_required
def mode_restart_page(request):
    """再稼働モード説明画面"""
    return render(request, "mode-restart.html")


@login_required
def mode_maintainimprove_page(request):
    """維持・向上モード説明画面"""
    return render(request, "mode-maintainimprove.html")

class ProfileView(TemplateView):
    template_name = "users/profile.html"