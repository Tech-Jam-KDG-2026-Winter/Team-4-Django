from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """カスタムユーザーモデル"""
    
    MODE_CHOICES = [
        ('restart', '再始動'),
        ('keep', '現状維持'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50, verbose_name='ユーザー名')
    mode = models.CharField(
        max_length=10,
        choices=MODE_CHOICES,
        default='restart',
        verbose_name='モード'
    )
    challenge_day = models.IntegerField(default=1, verbose_name='チャレンジ日数')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'
