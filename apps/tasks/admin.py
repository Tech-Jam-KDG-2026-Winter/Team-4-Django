from django.contrib import admin
from .models import TaskTemplate, DailyTask

@admin.register(TaskTemplate)
class TaskTemplateAdmin(admin.ModelAdmin):
    list_display = ['level', 'theme', 'title', 'created_at']
    list_filter = ['level', 'theme']
    search_fields = ['title', 'message']
    ordering = ['level']

@admin.register(DailyTask)
class DailyTaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'task_title', 'is_completed', 'created_at']
    list_filter = ['is_completed', 'date']
    search_fields = ['user__username', 'task_title']