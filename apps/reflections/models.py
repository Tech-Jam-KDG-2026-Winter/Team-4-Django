from django.db import models
from apps.users.models import User
from django.utils import timezone

class DailyReflection(models.Model):
    """日次振り返り"""
    
    reflection_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reflections'
    )
    date = models.DateField(default=timezone.now, verbose_name='振り返り日付')
    
    # 社会性チェック
    hello_count = models.IntegerField(default=0, verbose_name='あいさつ回数')
    thanks_given = models.BooleanField(default=False, verbose_name='ありがとう言えた')
    thanks_received = models.BooleanField(default=False, verbose_name='ありがとう言われた')
    
    # 感情ログ
    good_thing = models.TextField(blank=True, verbose_name='嬉しかったこと')
    bad_thing = models.TextField(blank=True, verbose_name='嫌だったこと')
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'daily_reflections'
        verbose_name = '日次振り返り'
        unique_together = ['user', 'date']
        ordering = ['-date']


class FeedbackMessage(models.Model):
    """振り返り後のフィードバック"""
    
    feedback_id = models.AutoField(primary_key=True)
    reflection = models.OneToOneField(
        DailyReflection,
        on_delete=models.CASCADE,
        related_name='feedback'
    )
    feedback_text = models.TextField(verbose_name='フィードバック文')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'feedback_messages'
        verbose_name = 'フィードバック'