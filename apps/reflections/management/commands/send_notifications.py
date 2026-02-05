from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from apps.users.models import User
from apps.reflections.services import send_email
import pytz


class Command(BaseCommand):
    help = 'タスク・振り返り時刻の通知メールを送信'

    def handle(self, *args, **options):
        # 日本時間で現在時刻を取得
        jst = pytz.timezone('Asia/Tokyo')
        now_jst = timezone.now().astimezone(jst)
        current_time = now_jst.time()
        
        # デバッグ出力
        self.stdout.write(f"現在時刻（JST）: {current_time}")
        
        users = User.objects.filter(email__isnull=False).exclude(email='')
        
        self.stdout.write(f"対象ユーザー数: {users.count()}")
        
        for user in users:
            self.stdout.write(f"ユーザー: {user.username}, task_time: {user.task_time}")
            
            # タスク通知（task_timeの5分前に送信）
            if user.task_time:
                task_notification_time = self.subtract_minutes(user.task_time, 5)
                self.stdout.write(f"  → タスク通知時刻: {task_notification_time}")
                
                if self.is_time_match(current_time, task_notification_time):
                    self.send_task_notification(user)
            
            # 振り返り通知（reflection_timeの5分前に送信）
            if user.reflection_time:
                reflection_notification_time = self.subtract_minutes(user.reflection_time, 5)
                self.stdout.write(f"  → 振り返り通知時刻: {reflection_notification_time}")
                
                if self.is_time_match(current_time, reflection_notification_time):
                    self.send_reflection_notification(user)
    
    def subtract_minutes(self, time_obj, minutes):
        """時刻からN分引く"""
        dt = datetime.combine(datetime.today(), time_obj)
        result = dt - timedelta(minutes=minutes)
        return result.time()
    
    def is_time_match(self, time1, time2):
        """時刻が一致するかチェック（分単位）"""
        return (time1.hour == time2.hour and 
                time1.minute == time2.minute)
    
    def send_task_notification(self, user):
        """タスク通知メール送信"""
        subject = f"🌊 {user.username}さん、今日のタスクの時間です"
        body = f"""
        <html>
        <body style="font-family: sans-serif; padding: 20px;">
            <h2>🌊 Yurage</h2>
            <p>こんにちは、{user.username}さん！</p>
            <p>今日のタスクを始める時間になりました。</p>
            <p>ゆっくりでいいので、一歩ずつ進んでいきましょう。</p>
            <a href="http://localhost:8000/task-today/" 
               style="display: inline-block; 
                      margin-top: 15px; 
                      padding: 12px 24px; 
                      background: #1B263B; 
                      color: white; 
                      text-decoration: none; 
                      border-radius: 25px;">
                タスクを見る
            </a>
        </body>
        </html>
        """
        
        success, error = send_email(
            to_email=user.email,
            subject=subject,
            body=body,
            is_html=True
        )
        
        if success:
            self.stdout.write(
                self.style.SUCCESS(f'タスク通知送信成功: {user.username} ({user.email})')
            )
        else:
            self.stdout.write(
                self.style.ERROR(f'タスク通知送信失敗: {user.username} - {error}')
            )
    
    def send_reflection_notification(self, user):
        """振り返り通知メール送信"""
        subject = f"�� {user.username}さん、振り返りの時間です"
        body = f"""
        <html>
        <body style="font-family: sans-serif; padding: 20px;">
            <h2>🌊 Yurage</h2>
            <p>こんにちは、{user.username}さん！</p>
            <p>今日の振り返りをする時間になりました。</p>
            <p>今日はどんな一日でしたか？</p>
            <a href="http://localhost:8000/review-1/" 
               style="display: inline-block; 
                      margin-top: 15px; 
                      padding: 12px 24px; 
                      background: #1B263B; 
                      color: white; 
                      text-decoration: none; 
                      border-radius: 25px;">
                振り返りを始める
            </a>
        </body>
        </html>
        """
        
        success, error = send_email(
            to_email=user.email,
            subject=subject,
            body=body,
            is_html=True
        )
        
        if success:
            self.stdout.write(
                self.style.SUCCESS(f'振り返り通知送信成功: {user.username} ({user.email})')
            )
        else:
            self.stdout.write(
                self.style.ERROR(f'振り返り通知送信失敗: {user.username} - {error}')
            )
