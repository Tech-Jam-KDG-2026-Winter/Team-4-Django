from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """カスタムユーザー管理"""
    list_display = ['username', 'email', 'mode', 'challenge_day', 'last_task_date', 'is_staff', 'created_at']
    list_filter = ['mode', 'is_staff', 'is_superuser', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['-created_at']
    
    # 編集画面のフィールド設定
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Drift Jellyfish 設定', {
            'fields': ('mode', 'challenge_day', 'task_time', 'reflection_time', 'last_task_date')
        }),
    )
    
    # 新規追加画面のフィールド設定
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Drift Jellyfish 設定', {
            'fields': ('mode', 'challenge_day', 'task_time', 'reflection_time')
        }),
    )