from rest_framework import serializers
from .models import TaskTemplate, DailyTask

class TaskTemplateSerializer(serializers.ModelSerializer):
    """タスクテンプレート用"""
    class Meta:
        model = TaskTemplate
        fields = ['id', 'level', 'theme', 'title', 'message']

class DailyTaskSerializer(serializers.ModelSerializer):
    """日次タスク用"""
    class Meta:
        model = DailyTask
        fields = [
            'task_id',
            'task_title',
            'task_message',
            'is_completed',
            'date',
            'completed_at',
            'created_at'
        ]
        read_only_fields = ['task_id', 'created_at']

       
