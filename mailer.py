# base module imports
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
import os

PREFS = json.load(open("preferences.json", encoding="utf-8"))

port = PREFS["smtpMail"]["port"]
smtp_server = PREFS["smtpMail"]["smtpServer"]
receiver_email = PREFS["hausmeisterMail"]
sender_email = os.environ["PYTHON_MAIL_USER"]
password = os.environ["PYTHON_MAIL_PASSWORD"]


def request(goods, comment):
    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    message.attach(
        MIMEText(f"""\
    Angeforderte Güter: {", ".join(goods)}
    Kommentar: {comment}
        """, "plain")
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
