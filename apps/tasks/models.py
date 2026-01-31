from django.db import models
from apps.users.models import User
from django.utils import timezone

class DailyTask(models.Model):
    """日次タスク"""
    
    task_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    date = models.DateField(default=timezone.now, verbose_name='タスク日付')
    task_title = models.CharField(max_length=100, verbose_name='タスク名')
    task_message = models.TextField(verbose_name='励ましメッセージ')
    is_completed = models.BooleanField(default=False, verbose_name='完了フラグ')
    completed_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='完了日時'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'daily_tasks'
        verbose_name = '日次タスク'
        ordering = ['-date']