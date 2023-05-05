# base module imports
import os
import random
import datetime

# external module imports
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError

# file imports
import block
import views

# constants
WELCOME_CHANNEL_ID = "C056K5MTRG9"

# load environment variables from .env file
load_dotenv()

# initialize app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# utility functions
def get_timestamp(days: int):
    date = datetime.datetime.now() + datetime.timedelta(days=0, seconds=20)
    # date = date.replace(hour=11, minute=0, second=0, microsecond=0)
    return int(date.timestamp())


@app.event("channel_join")
def channel_join():
    pass


# events
@app.event("team_join")
def team_join(event, say, client):
    user_id = event["user"]["id"]
    say(
        blocks=block.welcome(user_id=user_id),
        text=f"Willkommen zum Team, <@{user_id}>! 🎉",
        channel=WELCOME_CHANNEL_ID
    )

    try:
        client.chat_scheduleMessage(
            channel=WELCOME_CHANNEL_ID,
            post_at=get_timestamp(7),
            text=f"<@{user_id}> Du bist bereits seit einer Woche bei uns! \n"
                 "Um unseren Einstellungsprozess fortlaufend verbessern zu können, "
                 "freuen wir uns über dein Feedback.\n"
                 "Wir möchten dich deshalb bitten, an folgender Umfrage teilzunehmen:\n"
                 "https://forms.office.com/r/JG15TiBMED"
        )
    except SlackApiError as e:
        print(e)

    try:
        client.chat_scheduleMessage(
            channel=WELCOME_CHANNEL_ID,
            post_at=get_timestamp(9),
            text="<@{user_id}> denke bitte daran die Umfrage zur RomeisIE auszufüllen, "
                 "falls Du das noch nicht getan hast."
        )
    except SlackApiError as e:
        print(e)


# commands
@app.command("/hilfe")
def com_hilfe(ack):
    ack(
        "*Befehlsliste*\n\n"
        "`/internship-form`\n"
        "Gibt den Link zum Erfassungsformular für Praktikanten an.\n\n"
        "`/wlan`\n"
        "Gibt das W-Lan Passwort in Gelnhausen an.\n\n"
        "`/wlan-koeln`\n"
        "Gibt das W-Lan Passwort in Köln an.\n\n"
        "`/ci`\n"
        "Listet verschiedene Farb-Hex-Codes auf.\n\n"
        "`/coffee`\n"
        "Leistet Hilfestellung zur Beschaffung eines Kaffes."
    )


@app.command("/internship-form")
def com_internship_form(ack):
    ack(f"Das Erfassungsformular für Praktikanten findest Du unter dem folgenden Link: \n"
        f"https://forms.gle/AGcRqn3GNaWsucrQA")


@app.command("/wlan")
def com_wlan(ack):
    ack(f"Das W-Lan Passwort Gelnhausen lautet `NtyI4nDX2uYXh0V`")


@app.command("/wlan-koeln")
def com_wlan_koeln(ack):
    ack(f"Das W-Lan Passwort Köln lautet `Renkler2021`")


@app.command("/ci")
def com_ci(ack):
    ack(f"Green `#99cc33` \n"
        f"Alternate Green `#6bb200` \n"
        f"Grey `#A7a8aB` \n"
        f"White `#FFFFFF` \n"
        f"Dark Grey `#707070` \n"
        f"Light Black `#191919`")


@app.command("/coffee")
def com_coffee(ack):
    if random.randint(0, 2):
        ack(f"service@ws-kaffee.de")
    else:
        ack("`418` I'm a teapot\n"
            "The server refuses to brew coffee because it is, permanently, a teapot.\n"
            "service@ws-kaffee.de")


@app.message('open_modal')
def mes_open_modal(say):
    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Test Test"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a section block with a button."
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Click Me",
                        "emoji": True
                    },
                    "value": "click_me_123",
                    "action_id": "open_modal_button"
                }
            }
        ],
        text="button"
    )


# modals
@app.action("open_modal_button")
def open_modal(ack, body, client):
    # Acknowledge the command request
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view=views.umfrage_einstellungsprozess()
    )


# start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
