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
Gibt dir einen zufälligen Funfact an.

``/add-funfact [FUNFACT]``<br>
Fügt einen neuen Funfact hinzu.

``/remove-funfact [Index]``<br>
Entfernt einen Funfact.

``/praise [USER] [MSG(opt.)]``<br>
Mit diesem Befehl kannst du jemanden Loben.

### Begrüßung

Wenn jemand dem Slack-Workspace beitritt, wird er/sie mit einer Willkommensnachricht begrüßt.

### Umfrage

Sieben Tage nach dem Beitritt in den Workspace wird ein Mitglied gebeten, eine Umfrage zur RomeisIE auszufüllen.<br>
Zwei Tage nach letzterer Aufforderung wird das Mitglied nochmals daran erinnert, die Umfrage auszufüllen.

