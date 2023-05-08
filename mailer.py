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
        MIMEText(f"""\
Sehr geehrter Hausmeister,

könnten sie zur RomeisIE im Triangulum bitte {", ".join(goods)} bringen?

{comment}

Vielen Dank im Voraus für Ihre Unterstützung.

Mit freundlichen Grüßen,
RomeisIE Information Engineering

---------

Dies ist eine automatisch generierte Mail.
        """, "plain")
    )

    message.attach(
        MIMEText(f"""\
<html>
  <body>
    <p>Sehr geehrter Hausmeister,<br><br>
       könnten sie zur RomeisIE im Triangulum bitte {", ".join(goods)} bringen?<br><br>
       {comment}<br><br>
       Vielen Dank im Voraus für Ihre Unterstützung.<br><br>
       Mit freundlichen Grüßen,<br>
       RomeisIE Information Engineering<br><br>
       <hr><br><br>
       <i>Dies ist eine automatisch generierte Mail.</i>
    </p>
  </body>
</html>
        """, "html")
    )

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
