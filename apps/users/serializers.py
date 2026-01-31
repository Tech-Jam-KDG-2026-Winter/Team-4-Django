from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    """ユーザー登録用"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']  # ← modeを削除
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "パスワードが一致しません"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            # mode は指定しない（自動で None になる）
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
        """少なくとも1つは指定されている必要がある"""
        if not data.get('task_time') and not data.get('reflection_time'):
            raise serializers.ValidationError(
                'task_time または reflection_time を指定してください'
            )
        return data

class UserSerializer(serializers.ModelSerializer):
    """ユーザー情報取得用"""
    class Meta:
        model = User
        fields = ['user_id', 'username', 'mode', 'challenge_day', 'task_time','reflection_time','created_at']
        read_only_fields = ['user_id', 'created_at']