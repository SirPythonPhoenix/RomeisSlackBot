# base module imports
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os

# external module imports
from dotenv import load_dotenv

load_dotenv()
PREFS = json.load(open("preferences.json", encoding="utf-8"))
with open("mails/hausmeister-mail.txt", encoding="utf-8") as f:
    MAIL_TXT = f.read()
with open("mails/hausmeister-mail.html", encoding="utf-8") as f:
    MAIL_HTML = f.read()

port = PREFS["smtpMail"]["port"]
smtp_server = PREFS["smtpMail"]["smtpServer"]
receiver_email = PREFS["hausmeisterMail"]
sender_email = os.environ["PYTHON_MAIL_USER"]
password = os.environ["PYTHON_MAIL_PASSWORD"]


def request(goods, comment):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Anfrage"
    message["From"] = f'noreply <{sender_email}>'
    message["To"] = receiver_email

    message.attach(
        MIMEText(MAIL_TXT.format(", ".join(goods), comment), "plain")
    )

    message.attach(
        MIMEText(MAIL_HTML.format(", ".join(goods), comment), "html")
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
