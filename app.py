# base module imports
import os
import random
import datetime
import time
import json
import threading

# external module imports
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk.errors import SlackApiError

# file imports
import block
import views
import home
import mailer
import bingo_generator

# constants
PREFS = json.load(open("preferences.json", encoding="utf-8"))
DEV_MODE = PREFS["devMode"]
WELCOME_CHANNEL_ID = PREFS["welcomeChannelId"]
SEND_FEEDBACK_TO = PREFS["sendFeedbackSheetToChannels"]

# load environment variables from .env file
load_dotenv()

# initialize app
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


# utility functions
def get_timestamp(days: int):
    if DEV_MODE:
        date = datetime.datetime.now() + datetime.timedelta(seconds=20)
        return int(date.timestamp())
    else:
        date = datetime.datetime.now() + datetime.timedelta(days=days)
        date = date.replace(hour=PREFS["feedbackMessageClockHour"], minute=0, second=0, microsecond=0)
        return int(date.timestamp())


def load_data():
    global data
    data = json.load(open("data.json", "r", encoding="utf-8"))


def save_data():
    global data
    json.dump(data, open("data.json", "w", encoding="utf-8"))


# load data
if PREFS["restoreDataBackup"]:
    data = json.load(open("data-backup.json"))
    save_data()
else:
    data = {}
    load_data()


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
            channel=user_id,
            post_at=get_timestamp(PREFS["daysTillFeedback"]),
            text=f"<@{user_id}> Du bist bereits seit einer Woche bei uns! \n"
                 "Um unseren Einstellungsprozess fortlaufend verbessern zu können, "
                 "freuen wir uns über dein Feedback.\n"
                 "Wir möchten dich deshalb bitten, an unserem Feedback-Bogen teilzunehmen.",
            blocks=block.feedback_bogen(user_id)
        )
    except SlackApiError as e:
        print(e)

    try:
        client.chat_scheduleMessage(
            channel=user_id,
            post_at=get_timestamp(PREFS["daysTillFeedbackReminder"]),
            text=f"<@{user_id}> denke bitte daran die Umfrage zur RomeisIE auszufüllen, "
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
        "`/funfact`\n"
        "Gibt einen zufälligen Funfact aus.\n\n"
        "`/add-funfact [FUNFACT]`\n"
        "Fügt einen neuen Funfact hinzu.\n\n"
        "`/remove-funfact [ID]`\n"
        "Entfernt einen Funfact.\n\n"
        "`/hausmeister`\n"
        "Öffnet das Hausmeister-Menü\n\n"
        "`/kuche-roulette`\n"
        "Teilnahme am Kuchen-Roulette\n\n"
        "`/kuchen`\n"
        "Beginnt das Roulette.\n\n"
        "`/bingo-card`\n"
        "Generiert eine zufällige Bingo-Karte.\n\n"
        "`/add-bingo-phrase`\n"
        "Fügt eine Bingo-Phrase hinzu.\n\n"
        "`/remove-bingo-phrase`\n"
        "Entfernt eine Bingo-Phrase.\n\n"
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


@app.command("/kuchen-roulette")
def com_cake_roulette(ack, body, say):
    load_data()
    user_id = body['user_id']
    ack()
    if user_id in data["kuchenRouletteTeilnehmer"]:
        say(
            blocks=block.roulette_participiant(data["kuchenRouletteTeilnehmer"]),
            text="Teilnahme am Kuchen-Roulette."
        )
    else:
        say(
            blocks=block.roulette_intro(data["kuchenRouletteTeilnehmer"]),
            text="Teilnahme am Kuchen-Roulette."
        )


@app.command("/funfact")
def com_funfact(say, body, ack):
    user_id = body["user_id"]
    ack()
    load_data()
    funfact = random.choice(data['funfacts'])
    say(
        text=f"<@{user_id}> *Dein random funfact:*\n"
             f"{funfact['text']} _(id{funfact['id']})_"
    )


@app.command("/add-funfact")
def com_funfact(say, body, ack, command):
    load_data()
    funfact = {
        "id": data["funfactIdCounter"],
        "text": command["text"]
    }
    data["funfactIdCounter"] += 1
    data["funfacts"].append(funfact)
    save_data()
    user_id = body["user_id"]
    ack()
    say(
        text=f"<@{user_id}> *Folgender Funfact wurde erfolgreich hinzugefügt:*\n"
             f"{funfact['text']} _(id{funfact['id']})_"
    )


@app.command("/remove-funfact")
def com_funfact(body, ack, command):
    funfact_id = command["text"]
    load_data()
    user_id = body["user_id"]
    try:
        data["funfacts"] = [funfact for funfact in data["funfacts"] if funfact["id"] != int(funfact_id)]
        save_data()
        ack(
            text=f"<@{user_id}> *Funfact mit der ID #{funfact_id} wurde entfernt.*\n"
        )
    except ValueError:
        ack(
            text=f"<@{user_id}> Bitte gib eine valide Zahl an."
        )


@app.command("/hausmeister")
def com_hausmeister(body, ack, client):
    ack()
    load_data()
    last_request = data["lastHausmeisterRequest"]
    if last_request:
        last_request = datetime.datetime.fromtimestamp(last_request)
    client.views_open(
        trigger_id=body["trigger_id"],
        view=views.hausmeister(last_request)
    )


@app.command("/bingo-card")
def com_bingo_card(body, ack, say, client):
    ack()
    bingo_generator.generate_bingo(data["bingoPhrases"])
    say(
        text=f"Hier ist deine Bingo Card <@{body['user_id']}>"
    )
    client.files_upload_v2(
        file="bingo_card.png",
        channel=body["channel_id"]
    )


@app.command("/add-bingo-phrase")
def com_funfact(say, body, ack, command):
    bingo_phrase = command["text"]
    if bingo_phrase == "":
        ack("Bitte gib ein Argument ein.")
        return
    load_data()
    data["bingoPhrases"].append(bingo_phrase)
    save_data()
    user_id = body["user_id"]
    ack()
    say(
        text=f"<@{user_id}> *Folgende Bingo-Phrase wurde erfolgreich hinzugefügt:*\n{bingo_phrase}"
    )


@app.command("/remove-bingo-phrase")
def com_funfact(say, body, ack, command):
    bingo_phrase = command["text"]
    if bingo_phrase == "":
        ack("Bitte gib ein Argument ein.")
        return
    load_data()
    data["bingoPhrases"].remove(bingo_phrase)
    save_data()
    user_id = body["user_id"]
    ack()
    say(
        text=f"<@{user_id}> *Folgende Bingo-Phrase wurde erfolgreich entfernt:*\n{bingo_phrase}"
    )


@app.command("/kuchen")
def com_kuchen(ack, say):
    load_data()
    if len(data["kuchenRouletteTeilnehmer"]):
        user_id = random.choice(data["kuchenRouletteTeilnehmer"])
        ack()
        say(
            text=f"<@{user_id}> wurde zum Kuchen-Bäcker ausgelost!"
        )
        say(
            text=f"Du musst einen Kuchen backen (besorgen). Bitte bringe bei Gelegenheit einen Kuchen mit.",
            channel=user_id
        )
    else:
        ack(
            text="Zurzeit nimmt leider niemand am Kuchen-Roulette teil."
        )


# actions
@app.action("roulette_participate")
def action_rolette_participate(ack, body, say):
    load_data()
    user_id = body["user"]["id"]
    if user_id not in data['kuchenRouletteTeilnehmer']:
        data['kuchenRouletteTeilnehmer'].append(user_id)
        save_data()
        ack()
        say(
            text=f"Du bist nun einer von {len(data['kuchenRouletteTeilnehmer'])} "
                 f"Teilnehmern des Kuchen-Roulettes.",
            channel=user_id
        )
    else:
        ack()
        say(
            text=f"Du nimmst bereits am Kuchen-Roulette teil. Man kann leider nicht zwei mal teilnehmen...",
            channel=user_id
        )


@app.action("roulette_leave")
def action_rolette_participate(ack, body, say):
    load_data()
    user_id = body["user"]["id"]
    if user_id in data['kuchenRouletteTeilnehmer']:
        data['kuchenRouletteTeilnehmer'].remove(user_id)
        save_data()
        ack()
        say(
            text=f"Du bist nun kein Teilnehmer mehr beim Kuche-Roulette.",
            channel=user_id
        )
    else:
        ack()
        say(
            text=f"Du bist bereits kein Teilnehmer des Kuchen-Roulettes.",
            channel=user_id
        )


@app.action("einstellungsprozess_oeffnen")
def action_open_modal_button(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view=views.umfrage_einstellungsprozess()
    )


# view submits
@app.view("einstellungsprozess_submit")
def dm_button(ack, client, body, view):
    values = view["state"]["values"]
    user_id = body["user"]["id"]
    user_name = body["user"]["name"]
    ack()
    blocks = block.feedback_results(user_name, values)
    for channel in SEND_FEEDBACK_TO:
        client.chat_postMessage(
            channel=channel,
            text=f"*Ergebnisse des Feedbackbogens von {user_name}:*",
            blocks=blocks
        )
    client.chat_postMessage(channel=user_id, text="Der Umfragebogen wurde erfolgreich ausgefüllt und abgeschickt!")


@app.view("hausmeister_submit")
def dm_button(ack, client, body, view):
    values = view["state"]["values"]
    goods = [
        ":".join(good['text']['text'].split(':')[2:])[1:] for
        good in values['goods']['checkboxes-action']['selected_options']
    ]
    comment = values['comment']['plain_text_input-action']['value']
    comment = comment if comment else ""
    user_id = body["user"]["id"]
    ack()
    mailer.request(goods, comment)
    load_data()
    data["lastHausmeisterRequest"] = datetime.datetime.now().timestamp()
    save_data()
    client.chat_postMessage(channel=user_id,
                            text=f"Folgende Bestellung wurde soeben an den Hausmeister gesendet: {', '.join(goods)}\n"
                                 f"Kommentar: {comment if comment else '/'}")


# home
@app.event("app_home_opened")
def app_home(client, event):
    try:
        client.views_publish(
            user_id=event["user"],
            view=home.home()
        )
    except Exception as e:
        print(f"Error publishing home tab: {e}")


# threads


def morgens_meeting():
    while True:
        current_time = datetime.datetime.now()
        load_data()
        if current_time.weekday() < 5 and \
           current_time.hour == 8 and \
           current_time.minute in range(35, 43) and \
           current_time.weekday() != data["lastMorningRemider"]:
            data["lastMorningRemider"] = current_time.weekday()
            save_data()
            app.client.chat_postMessage(
                text="Das morgentliche Meeting im Huddle beginnt in wenigen Minuten.",
                channel=PREFS["morningMeetingChannelID"]
            )
        time.sleep(5)


threading.Thread(target=morgens_meeting).start()


# start app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
