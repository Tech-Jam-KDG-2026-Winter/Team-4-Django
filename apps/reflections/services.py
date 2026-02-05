import smtplib
from email.mime.text import MIMEText
from typing import Tuple


# ===== SMTP設定 (Gmail) =====

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

# Gmail アカウント情報
SMTP_USER = "hinato263@gmail.com"  # 自分のメールアドレス
SMTP_PASSWORD = "bgizxpmrgazhqmca"  # 作ったパスワード
def send_email(
    to_email: str,
    subject: str,
    body: str,
    *,
    is_html: bool = True,
    from_email: str | None = None,
) -> Tuple[bool, str | None]:
    """
    アプリ内から簡単に呼び出せる汎用メール送信関数。
 
    例:
        success, error = send_email(
            to_email="user@example.com",
            subject="タイトル",
            body="<p>本文</p>",
            is_html=True,
        )
    """
    if not to_email:
        return False, "送信先メールアドレスが指定されていません。"
 
    charset = "utf-8"
    subtype = "html" if is_html else "plain"
    msg = MIMEText(body, subtype, charset)
 
    msg["Subject"] = subject
    msg["From"] = from_email or SMTP_USER
    msg["To"] = to_email
 
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(SMTP_USER, SMTP_PASSWORD)
            smtp.sendmail(msg["From"], [to_email], msg.as_string())
        return True, None
    except Exception as e:
        # 本番ではログ出力などを行う
        return False, str(e)


def send_test_email(to_email: str) -> Tuple[bool, str | None]:
    """
    入力されたメールアドレス宛に、SMTPでテストメールを送信する。
    内部的には send_email() を利用する。
 
    戻り値:
        (success, error_message)
    """
    html_body = """
    <html>
      <body>
        <p>これは Django アプリから送信された <b>テストメール</b> です。</p>
        <p>SMTP 設定が正しく動作しているかの確認用です。</p>
      </body>
    </html>
    """
 
    return send_email(
        to_email=to_email,
        subject="SMTP テストメール",
        body=html_body,
        is_html=True,
    )


