from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import date
import random
from .models import TaskTemplate, DailyTask
from .serializers import DailyTaskSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_today_task(request):
    """今日のタスク取得"""
    user = request.user
    today = date.today()
    
    # モード未選択チェック
    if user.mode is None:
        return Response(
            {"error": "先にモードを選択してください"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # 今日のタスクが既に存在するか確認
    existing_task = DailyTask.objects.filter(user=user, date=today).first()
    if existing_task:
        return Response(
            {
                "message": "今日のタスク",
                "task": DailyTaskSerializer(existing_task).data
            },
            status=status.HTTP_200_OK
        )
    
    # challenge_day に応じたレベルを決定
    level = user.challenge_day
    
    # そのレベルのタスクテンプレートをランダムに選択
    templates = TaskTemplate.objects.filter(level=level)
    if not templates.exists():
        return Response(
            {"error": f"レベル{level}のタスクが見つかりません"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    template = random.choice(templates)
    
    # DailyTask を作成
    daily_task = DailyTask.objects.create(
        user=user,
        date=today,
        task_template=template,
        task_title=template.title,
        task_message=template.message,
        is_completed=False
    )
    
    return Response(
        {
            "message": "今日のタスクを生成しました",
            "task": DailyTaskSerializer(daily_task).data
        },
        status=status.HTTP_201_CREATED
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def complete_task(request, task_id):
    """タスク完了"""
    user = request.user
    
    try:
        task = DailyTask.objects.get(task_id=task_id, user=user)
    except DailyTask.DoesNotExist:
        return Response(
            {"error": "タスクが見つかりません"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if task.is_completed:
        return Response(
            {"error": "既に完了済みです"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # タスク完了
    task.is_completed = True
    task.completed_at = timezone.now()
    task.save()
    
    # challenge_day を +1
    user.challenge_day += 1
    user.save()
    
    return Response(
        {
            "message": "タスク完了！お疲れさまでした",
            "task": DailyTaskSerializer(task).data,
            "next_level": user.challenge_day
        },
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_task(request, task_id):
    """タスク変更"""
    user = request.user
    
    try:
        task = DailyTask.objects.get(task_id=task_id, user=user)
    except DailyTask.DoesNotExist:
        return Response(
            {"error": "タスクが見つかりません"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if task.is_completed:
        return Response(
            {"error": "完了済みのタスクは変更できません"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # 現在のレベル
    level = user.challenge_day
    
    # そのレベルの全タスクテンプレート
    all_templates = list(TaskTemplate.objects.filter(level=level))
    
    if not all_templates:
        return Response(
            {"error": f"レベル{level}のタスクが見つかりません"},
            status=status.HTTP_404_NOT_FOUND
        )
    
    # 候補 = 全タスク - 変更済みリスト - 現在のタスク
    available_templates = [
        t for t in all_templates 
        if t.id not in task.changed_templates and t.id != task.task_template.id
    ]
    
    # 候補がなくなったら、最初に戻る（リストをリセット）
    if not available_templates:
        task.changed_templates = []
        # 現在のタスク以外を候補に
        available_templates = [
            t for t in all_templates 
            if t.id != task.task_template.id
        ]
    
    # ランダムに選択
    new_template = random.choice(available_templates)
    
    # 現在のテンプレートIDを変更済みリストに追加（新しいタスクに変更後）
    if task.task_template:
        current_id = task.task_template.id
        if current_id not in task.changed_templates:
            task.changed_templates.append(current_id)
    
    # タスクを更新
    task.task_template = new_template
    task.task_title = new_template.title
    task.task_message = new_template.message
    task.save()
    
    # 残り変更可能回数
    remaining = len(all_templates) - len(task.changed_templates)
    
    return Response(
        {
            "message": "タスクを変更しました",
            "task": DailyTaskSerializer(task).data,
            "remaining_changes": remaining
        },
        status=status.HTTP_200_OK
    )