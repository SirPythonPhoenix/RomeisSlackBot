# RomeisSlackBot

<img alt="Slackbot Logo" src="https://slack.com/img/product-ui-generator/apps/slackbot.png" width="100" style="border-radius: 20%">

## Overview

The purpose of this Slack app is to enhance the onboarding process for new employees and serve as a central hub for questions and information.

The application includes several helpful Slack commands and also provides an info page in the application's profile in Slack, listing all the commands.

## Setup

The required external Python modules are listed in [requirements.txt](requirements.txt) and can be installed using pip with the following command:<br>

```
pip install -r requirements.txt
```


Furthermore, it is necessary to set the OAuth environment variables `SLACK_BOT_TOKEN` and `SLACK_APP_TOKEN`. To do this, create a `.env` file at the root of this project and set the respective variables there.

To start the application, execute [app.py](app.py).

## Docs

### Commands

``/internship-form``<br>
Provides the link to the internship application form.

``/wlan``<br>
Provides the Wi-Fi password for Gelnhausen.

``/wlan-koeln``<br>
Provides the Wi-Fi password for Cologne.

``/ci``<br>
Lists various color hex codes.

``/coffee``<br>
Provides assistance in getting a coffee.

``/funfact``<br>
Displays a random fun fact.

``/add-funfact [FUNFACT]``<br>
Adds a new fun fact.

``/remove-funfact [ID]``<br>
Removes a fun fact.

``/hausmeister``<br>
Opens the janitor menu.

``/kuchen-roulette``<br>
Participates in the cake roulette.

``/kuchen``<br>
Starts the roulette.

``/bingo-card``<br>
Generates a random bingo card.

``/add-bingo-phrase``<br>
Adds a bingo phrase.

``/remove-bingo-phrase``<br>
Removes a bingo phrase.

### Greeting

When someone joins the Slack workspace, they are greeted with a welcome message.

### Survey

Seven days after joining the workspace, a member is asked to fill out a survey about RomeisIE.<br>
Two days after the initial request, the member is reminded again to complete the survey.

### Preferences

Basic configuration options are recorded in [preferences.json](preferences.json).

``devMode: bool``<br>
Reduces the time until the welcome message for new members if set to true.

``restoreDataBackup: bool``<br>
Overwrites [data.json](data.json) with [data-backup.json](data-backup.json) if set to true.

``hausmeisterMail: string``<br>
The email address of the janitor.

``smtpMail.port: int``<br>
Port for mail delivery.

``smtpMail.smtpServer: string``<br>
SMTP mail server. <br>
Note: The sender email address and password are stored as environment variables.

``welcomeChannelID: bool``<br>
Channel ID of the channel where new server members are greeted.

``sendFeedbackSheetToChannels: array<String>``<br>
Channel IDs (which can also be DM channels) or user IDs to which the feedback form result is sent.

``daysTillFeedback: int``<br>
Days until a new member is asked to fill out the feedback form.

``daysTillFeedbackReminder: int``<br>
Days until a new member is reminded to fill out the feedback form.

``feedbackMessageClockHour: int``<br>
Hour at which the member receives the feedback message.

``morningMeetingChannelID: string``<br>
Channel ID of the channel where a reminder for the morning meetings is sent.

### System Environment Variables

It is recommended to store the environment variables in a `.env` file.
The following environment variables must be set before using this bot:

``SLACK_BOT_TOKEN``<br>
The Slack bot's bot token.

``SLACK_APP_TOKEN``<br>
The Slack bot's application token.

``PYTHON_MAIL_USER``<br>
e.g., my-mail-address@gmail.com<br>
IMPORTANT: An SMTP access must be set up beforehand. 
The SMTP server is specified in [preferences.json](preferences.json).

``PYTHON_MAIL_PASSWORD``<br>
Password of the mail address.
