import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")   
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")    

def send_email_notification(subject, message):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
    print("[Real Email Notification Sent]")
    
