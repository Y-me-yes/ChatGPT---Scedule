"""
send_email.py
Sends a simple email using Gmail's SMTP server with an App Password.
"""

import smtplib
import ssl
from email.message import EmailMessage

# --- Configuration ---
SENDER_EMAIL = "govenoryusuf@gmail.com"
SENDER_APP_PASSWORD = "cyus yklj orho foqw"  # Gmail App Password
RECEIVER_EMAIL = "ayashicompany0@gmail.com"

SUBJECT = "May Allah Make Qatar Possible"

BODY = """Salaam Alaikum

May allah make QATAR possible for you.

Ameen."""


def build_message() -> EmailMessage:
    """Construct the email message object."""
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = SUBJECT
    msg.set_content(BODY)
    return msg


def send_email() -> None:
    """Connect to Gmail SMTP over SSL and send the message."""
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
        server.send_message(build_message())

    print("✅ Email sent successfully!")


if __name__ == "__main__":
    try:
        send_email()
    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed. Double-check the App Password and "
              "that 2-Step Verification is enabled on the sender account.")
    except smtplib.SMTPException as exc:
        print(f"❌ SMTP error: {exc}")
    except Exception as exc:
        print(f"❌ Unexpected error: {exc}")
