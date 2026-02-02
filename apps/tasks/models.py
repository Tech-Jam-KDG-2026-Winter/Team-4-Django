from django.db import models

class TaskTemplate(models.Model):
    """タスクマスター（テンプレート）"""
    
    THEME_CHOICES = [
        ('alone', '自分の部屋で、一人で'),
        ('family', '家の中で、家族と'),
        ('outside', '家の外へ'),
        ('stay_outside', '外で過ごす'),
        ('interact', '人と関わる'),
        ('exercise', '体を動かす'),
        ('challenge', '新しいことに挑戦'),
    ]
    
    level = models.IntegerField(
        verbose_name='レベル',
        help_text='1-50'
    )
    theme = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        verbose_name='テーマ'
    )
    title = models.CharField(
        max_length=100,
        verbose_name='タスク名'
    )
    message = models.TextField(
        verbose_name='メッセージ',
        help_text='ユーザーに表示する優しいメッセージ'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'task_templates'
        verbose_name = 'タスクテンプレート'
        verbose_name_plural = 'タスクテンプレート'
        ordering = ['level', 'id']
    
    def __str__(self):
        return f"Lv.{self.level} - {self.title}"





class DailyTask(models.Model):
    """ユーザーの日次タスク"""
    
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=100)
    task_message = models.TextField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='daily_tasks'
    )
    date = models.DateField()
    completed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    task_template = models.ForeignKey(
        TaskTemplate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='元のテンプレート'
    )
    
    # ← ここに追加
    changed_templates = models.JSONField(
        default=list,
        verbose_name='変更済みテンプレートIDリスト'
    )
    
    class Meta:
        db_table = 'daily_tasks'
        verbose_name = '日次タスク'
        verbose_name_plural = '日次タスク'
    
    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.task_title}"