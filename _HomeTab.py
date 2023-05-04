from slackeventsapi import SlackEventAdapter
import os
from slack_sdk.web import WebClient
from slack_bolt import App
from pathlib import Path
import logging
from dotenv import load_dotenv
from slack_sdk.errors import SlackApiError


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = WebClient("SLACK_BOT_TOKEN")
logger = logging.getLogger(__name__)

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)





@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
    
        client.views_publish(
           
            user_id=event["user"],
       
            view=
                
{
	"type": "home",
	"blocks": [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "Home Tab",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hier findest Du die wichitgsten Links um Dir den Einstieg bei romeisIE zu erleichtern."
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Linux"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Zur Webseite",
					
				},
				"value": "click_me_123",
				"url": "https://ubuntu.com/tutorials/command-line-for-beginners",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Hier findest Du einen Einstieg in die Linuxkommandozeile und die wichtigsten Begriffe.",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Linuxkommandozeile"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Zur Webseite",
					
				},
				"value": "click_me_123",
				"url": "https://www.digitalocean.com/community/tutorial_series/getting-started-with-linux",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Hier gibt es allgemeine Informationen rund um die Linuxkommandozeile.",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Git"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Zum Kurs",
					
				},
				"value": "click_me_123",
				"url": "https://open.hpi.de/courses/git2020",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Hier kannst Du einen Videokurs zu den wichtigsten Themengebieten in Git finden und den Einstieg in Github gezeigt bekommen.",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Docker"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Zur Webseite",
					
				},
				"value": "click_me_123",
				"url": "https://docs.docker.com/get-started/",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Hier findest Du von der Installation Docker's bis hin zur Entwicklung alles was Du brauchst um mit Docker erfolgreich starten und arbeiten kannst.",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "PHP 8.0"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Zum Guide ",
					
				},
				"value": "click_me_123",
				"url": "https://phptherightway.com/",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Auf dieser Seite findest Du einen Komplettguide von Anfang bis Ende zu PHP 8.0, unter anderem auch mit Beispielaufgaben",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Symfony"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Zur Webseite",
					
				},
				"value": "click_me_123",
				"url": "https://symfony.com/doc/current/getting_started/index.html",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Hier findest du eine Einleitung rund um das Thema Symfony.",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Doctrine"
			},
			"accessory": {
				"type": "button",
				"text": {
					"type": "plain_text",
					"text": "Zur Webseite",
					
				},
				"value": "click_me_123",
				"url": "https://www.doctrine-project.org/projects/doctrine-orm/en/2.8/tutorials/getting-started.html",
				"action_id": "button-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "Hier findest Du anfangend von Tutorials zum Start bis hin zu fortgeschrittenen Erklärungen rund um Doctrine alles.",
				
			}
		},
		{
			"type": "divider"
		},
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hier kannst Du alles finden um bei uns erfolgreich durchzustarten. Natürlich kannst Du diese Seite hier auch als Nachschlagewerk nutzen um dein Wissen so weiter zu vertiefen und auffrischen zu können."
			}
		}
	]
}








        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@app.event("app_home_opened")
def handle_app_home_opened_events(body,logger):
    logger.info(body)

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))