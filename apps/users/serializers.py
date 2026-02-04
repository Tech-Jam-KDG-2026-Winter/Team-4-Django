from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    """ユーザー登録用"""
    email = serializers.EmailField(required=False, allow_blank=True)  # 任意
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']  # email追加
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "パスワードが一致しません"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  # email を追加（空でもOK）
            password=validated_data['password']
        )
        return user

class ModeSelectionSerializer(serializers.Serializer):
    """モード選択用"""
    mode = serializers.ChoiceField(choices=['restart', 'keep'])
    
    def validate_mode(self, value):
        """モードの妥当性チェック"""
        if value not in ['restart', 'keep']:
            raise serializers.ValidationError('無効なモードです')
        return value

class LoginSerializer(serializers.Serializer):
    """ログイン用のシリアライザー"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        """ユーザー名とパスワードの検証"""
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            # Djangoの認証システムでユーザー確認
            user = authenticate(username=username, password=password)
            
            if user:
                if user.is_active:
                    data['user'] = user
                    return data
                else:
                    raise serializers.ValidationError('このアカウントは無効化されています')
            else:
                raise serializers.ValidationError('ユーザー名またはパスワードが正しくありません')
        else:
            raise serializers.ValidationError('ユーザー名とパスワードを入力してください')

class TimeSettingsSerializer(serializers.Serializer):
    """タスク・振り返り時刻設定用"""
    task_time = serializers.TimeField(
        required=False,
        help_text="タスク表示時刻（例: 05:00）"
    )
    reflection_time = serializers.TimeField(
        required=False,
        help_text="振り返り時刻（例: 20:00）"
    )
    
    def validate(self, data):
        """バリデーション"""
        from datetime import datetime, timedelta
        
        task_time = data.get('task_time')
        reflection_time = data.get('reflection_time')
        
        # 両方指定されている場合のみ時間チェック
        if task_time and reflection_time:
            # 仮の日付で時刻を作成
            t1 = datetime.combine(datetime.today(), task_time)
            t2 = datetime.combine(datetime.today(), reflection_time)
            
            # 振り返りがタスクより前または同じなら翌日扱い
            if t2 <= t1:
                t2 += timedelta(days=1)
            
            # 差を計算（時間）
            time_diff = (t2 - t1).total_seconds() / 3600
            
            # 24時間以上離れてたらNG
            if time_diff >= 24:
                raise serializers.ValidationError(
                    'タスクと振り返りの間隔は24時間未満にしてください'
                )
        
        # 少なくとも1つは指定されている必要がある
        if not task_time and not reflection_time:
            raise serializers.ValidationError(
                'task_time または reflection_time を指定してください'
            )
        
        return data

class AccountUpdateSerializer(serializers.Serializer):
    """アカウント情報編集用"""
    username = serializers.CharField(required=False, max_length=150)
    email = serializers.EmailField(required=False)
    current_password = serializers.CharField(required=False, write_only=True)
    new_password = serializers.CharField(required=False, write_only=True, validators=[validate_password])
    
    def validate(self, data):
        """バリデーション"""
        # パスワード変更の場合、current_password が必須
        if 'new_password' in data:
            if 'current_password' not in data:
                raise serializers.ValidationError({
                    "current_password": "パスワードを変更するには現在のパスワードが必要です"
                })
        
        return data
        
    
class UserSerializer(serializers.ModelSerializer):
    """ユーザー情報取得用"""
    class Meta:
        model = User
        fields = ['user_id', 'username', 'mode', 'challenge_day', 'task_time','reflection_time','last_task_date','created_at']
        read_only_fields = ['user_id', 'created_at']