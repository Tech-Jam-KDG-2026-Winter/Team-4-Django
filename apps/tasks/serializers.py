from rest_framework import serializers
from .models import TaskTemplate, DailyTask


class TaskTemplateSerializer(serializers.ModelSerializer):
    """タスクテンプレート用"""
    class Meta:
        model = TaskTemplate
        fields = ['id', 'level', 'theme', 'title', 'message', 'reflection_questions']


class DailyTaskSerializer(serializers.ModelSerializer):
    """日次タスク用"""
    # タスクテンプレートから reflection_questions を取得
    reflection_questions = serializers.SerializerMethodField()
    
    class Meta:
        model = DailyTask
        fields = [
            'task_id',
            'task_title',
            'task_message',
            'is_completed',
            'date',
            'completed_at',
            'created_at',
            'reflection_questions'  # 追加
        ]
        read_only_fields = ['task_id', 'created_at', 'reflection_questions']
    
    def get_reflection_questions(self, obj):
        """タスクテンプレートから振り返り質問を取得"""
        if obj.task_template and obj.task_template.reflection_questions:
            return obj.task_template.reflection_questions
        # デフォルトの質問（テンプレートにない場合）
        return [
            "挨拶ができた",
            "ありがとうを言えた",
            "感謝された"
        ]