from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

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


class UserLoginSerializer(serializers.Serializer):
    """ログイン用"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    """ユーザー情報取得用"""
    class Meta:
        model = User
        fields = ['user_id', 'username', 'mode', 'challenge_day', 'created_at']
        read_only_fields = ['user_id', 'created_at']
