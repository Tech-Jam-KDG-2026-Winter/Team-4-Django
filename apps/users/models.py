from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """カスタムユーザーモデル"""
    
    MODE_CHOICES = [
        ('restart', '再始動'),
        ('keep', '現状維持'),
    ]
    
    user_id = models.AutoField(primary_key=True)
    mode = models.CharField(
        max_length=10,
        choices=MODE_CHOICES,
        null=True,
        blank=True,
        verbose_name='モード'
    )
    challenge_day = models.IntegerField(default=1, verbose_name='チャレンジ日数')
    
    task_time = models.TimeField(
        default='05:00:00',
        verbose_name='タスク表示時刻'
    )
    reflection_time = models.TimeField(
        default='20:00:00',
        verbose_name='振り返り時刻'
    )
    
    # 追加：最後にタスクを完了した日
    last_task_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='最終タスク実施日'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 衝突回避
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='グループ'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='ユーザー権限'
    )
    
    class Meta:
        db_table = 'users'
        verbose_name = 'ユーザー'
        verbose_name_plural = 'ユーザー'