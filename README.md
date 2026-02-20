# Drift Jellyfish（Yurage）

**Drift Jellyfish**（内部名称: Yurage）は、日々の小さなタスクと振り返りを通じて、少しずつ習慣を築いていき、「努力せず健康」を目指して作成されたアプリです。

## 作成経緯
このアプリはブルーウェールチャレンジというかつて、人を強く動かしてしまったあるゲームの構造に着目しました。私たちはその「人が動く仕組み」を、破壊ではなく回復のために使えないかと考えました。思春期・反抗期が重なる時期に、考えなくても少しずつ整っていく体験を届けたい。そんな思いから、このアプリは生まれました。

## 概要

このアプリは、毎日1つのタスクに取り組み、その日の振り返りを行うことで、自分のペースで着実に前進できるようサポートします。レベル1〜50の段階的なタスク設計により、「再始動モード」と「現状維持モード」の2つのモードから、自分に合った進め方を選べます。

## 主な機能

- **ユーザー認証** - サインアップ、ログイン、プロフィール、ログアウト
- **モード選択** - 再始動（ゼロから）or 現状維持（続きから）を選択
- **デイリータスク** - 1日1タスク、レベルに応じた3テーマからランダムに表示
- **振り返り** - YES/NOの質問と自由記述で1日を振り返る
- **メール通知** - タスク・振り返り時刻のリマインド（オプション）

### タスクシステム

- 50レベル × 各レベル3タスク
- テーマ: 一人で・家族と・外出・外に滞在・交流・運動・チャレンジ
- 1日に1回だけタスクを変更可能
- 3日以上サボった場合：
  - 再始動モード → レベル1にリセット
  - 現状維持モード → レベル8に調整

### 振り返り

- タスクごとのYES/NO質問（最大3問）
- 「ありがとう」の回数、良かったこと・困ったことの自由記述
- 振り返り後のフィードバックメッセージ

## 技術スタック

| カテゴリ | 技術 |
|---------|------|
| フレームワーク | Django 6.0.1 |
| API | Django REST Framework 3.16.1 |
| データベース | SQLite |
| 認証 | トークン + セッション |
| メール | SMTP（Gmail） |

## セットアップ

### 1. 仮想環境の作成と有効化

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 依存関係のインストール

```bash
pip install -r requirements.txt
```

> **補足**: メール通知機能を使う場合は `pytz` を追加でインストールしてください: `pip install pytz`

### 3. データベースのマイグレーション

```bash
python manage.py migrate
```

### 4. タスクのマスターデータを投入（任意）

レベル1〜50のタスクテンプレートを投入する場合：

```bash
sqlite3 db.sqlite3 < data/tasks_data.sql
```

### 5. 開発サーバーの起動

```bash
python manage.py runserver
```

`http://localhost:8000/` でアクセスできます。

### 管理画面

- URL: `http://localhost:8000/admin/`
- スーパーユーザーの作成: `python manage.py createsuperuser`

## メール通知の設定（オプション）

タスク・振り返りのリマインダーをメールで送信する場合：

1. `apps/reflections/services.py.example` を `services.py` にコピー
2. Gmailのアドレスとアプリパスワードを設定
3. cron等で以下を定期実行（例: 5分ごと）

```bash
python manage.py send_notifications
```

> **セキュリティ**: `services.py` には認証情報が含まれるため、本番環境では環境変数やシークレット管理を推奨します。

## 主なURL

| パス | 説明 |
|------|------|
| `/` | サービス稼働確認（JSON） |
| `/login/` | ログイン |
| `/signup/` | サインアップ |
| `/profile/` | プロフィール |
| `/mode-question/` | モード選択 |
| `/task-today/` | 今日のタスク |
| `/review-1/`, `/review-2/` | 振り返り |
| `/api/users/` | ユーザーAPI |
| `/api/tasks/` | タスクAPI |
| `/api/reflections/` | 振り返りAPI |

## プロジェクト構造

```
Techjam-Team4/
├── manage.py
├── requirements.txt
├── config/                # プロジェクト設定
│   ├── urls.py
│   └── settings/
├── apps/
│   ├── users/             # 認証・プロフィール・モード設定
│   ├── tasks/             # デイリータスク
│   ├── reflections/       # 振り返り・メール通知
│   └── common/
├── templates/             # HTMLテンプレート
├── static/                # CSS等
└── data/
    └── tasks_data.sql     # タスクマスターデータ
```

## 環境設定

開発時は `config.settings.local` が使用されます。本番デプロイ時は環境変数で `DJANGO_SETTINGS_MODULE` を `config.settings.prod` に設定してください。

## ライセンス

Techjam Team4 プロジェクト
