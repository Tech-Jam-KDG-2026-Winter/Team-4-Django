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
        fields = ['username', 'password', 'password_confirm', 'mode']
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "パスワードが一致しません"})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            mode=validated_data.get('mode', 'restart')
        )
        return user


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


class UserSerializer(serializers.ModelSerializer):
    """ユーザー情報取得用"""
    class Meta:
        model = User
        fields = ['user_id', 'username', 'mode', 'challenge_day', 'created_at']
        read_only_fields = ['user_id', 'created_at']