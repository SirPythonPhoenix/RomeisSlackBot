# RomeisSlackBot

<img alt="Slackbot Logo" src="https://slack.com/img/product-ui-generator/apps/slackbot.png" width="100" style="border-radius: 20%">

## Overview

Ziel dieser Slack-App ist, den OnBoarding Prozess von neuen Mitarbeitenden zu verbessern und eine zentrale Anlaufstelle für Fragen und Informationen zu sein.

Die Applikation umfasst daher einige hilfreiche Slack-Commands, aber auch eine Info-Seite im Profil der Anwendung in Slack mit einem Bereich für häufig gestellte Fragen.

## Setup

Benötigte externe Python-Module sind in der [requirements.txt](requirements.txt) aufgeführt und können durch pip mit folgendem Befehl installiert werden:<br>
````
pip install -r requirements.txt
````

Des Weiteren ist es nötig, die OAuth Umgebungsvariablen ``SLACK_BOT_TOKEN`` und ``SLACK_APP_TOKEN`` zu setzen. Legen sie dafür im root dieses Projektes eine ``.env`` an setzen sie darin die entsprechenden Variablen.

Zum Starten der Applikation muss nun die [app.py](app.py) ausgeführt werden. 

## Docs

### Commands

``/internship-form``<br>
Gibt den Link zum Erfassungsformular für Praktikanten an.

``/wlan``<br>
Gibt das W-Lan Passwort in Gelnhausen an.

``/wlan-koeln``<br>
Gibt das W-Lan Passwort in Köln an.

``/ci``<br>
Listet verschiedene Farb-Hex-Codes auf.

``/coffee``<br>
Leistet Hilfestellung zur Beschaffung eines Kaffes.

``/funfact``<br>
Gibt einen zufälligen Funfact aus.

``/add-funfact [FUNFACT]``<br>
Fügt einen neuen Funfact hinzu.

``/remove-funfact [ID]``<br>
Entfernt einen Funfact.

``/hausmeister``<br>
Öffnet das Hausmeister-Menü

``/kuchen-roulette``<br>
Teilnahme am Kuchen-Roulette.

``/kuchen``<br>
Beginnt das Roulette.

``/bingo-card``<br>
Generiert eine zufällige Bingo-Karte.

``/add-bingo-phrase``<br>
Fügt eine Bingo-Phrase hinzu.

``/remove-bingo-phrase``<br>
Entfernt eine Bingo-Phrase.

### Begrüßung

Wenn jemand dem Slack-Workspace beitritt, wird er/sie mit einer Willkommensnachricht begrüßt.

### Umfrage

Sieben Tage nach dem Beitritt in den Workspace wird ein Mitglied gebeten, eine Umfrage zur RomeisIE auszufüllen.<br>
Zwei Tage nach letzterer Aufforderung wird das Mitglied nochmals daran erinnert, die Umfrage auszufüllen.

### Preferences

Grundlegende Einstellungsmöglichkeiten sind in der [preferences.json](preferences.json) erfasst.

``devMode: bool``<br>
Senkt die Zeit bis zur Begrüßungsnachricht neuer Mitglieder, falls true.

``restoreDataBackup: bool``<br>
Überschreibt [data.json](data.json) mit [data-backup.json](data-backup.json), falls true.

``hausmeisterMail: string``<br>
Die Mail-Adresse des Hausmeisters.

``smtpMail.port: int``<br>
Port für den Mailversand.

``smtpMail.smtpServer: string``<br>
SMTP-Mail Server. <br>
Info: Die Sender-Mail-Adresse und das Passwort sind als Environment-Variables gespeichert.

``welcomeChannelID: bool``<br>
ChannelID des Channels, in dem neue Server-Mitglieder begrüßt werden.

``sendFeedbackSheetToChannels: array<String>``<br>
ChannelID's (das können auch DM-Channel sein) oder UserID's and die das Resultat des Feedback-Bogens gesendet wird.

``daysTillFeedback: int``<br>
Tage, bis ein neuer Member darum gebeten wird, das Feedback-Formular auszufüllen.

``daysTillFeedbackReminder: int``<br>
Tage, bis ein neuer Member erinnert wird, das Feedback-Formulr auszufüllen.

``feedbackMessageClockHour: int``<br>
Stunde zu der der Member die Feedback-Nachricht erhällt.

``morningMeetingChannelID: string``<br>
ChannelID des Channels in den ein Reminder zum morgentlichen Meetings gesendet wird.

