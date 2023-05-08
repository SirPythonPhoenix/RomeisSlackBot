def home():
    return {
        "type": "home",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Befehlsliste",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Im folgenden finden sie eine Befehlsliste dieses Slack-Bots. "
                            "Für mehr Informationen können sie sich das "
                            "<https://github.com/SirPythonPhoenix/RomeisSlackBot|Github-Repo> anschauen."
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "`/internship-form`\nGibt den Link zum Erfassungsformular für Praktikanten an.\n\n"
                            "`/wlan`\nGibt das W-Lan Passwort in Gelnhausen an.\n\n"
                            "`/wlan-koeln`\nGibt das W-Lan Passwort in Köln an.\n\n"
                            "`/ci`\nListet verschiedene Farb-Hex-Codes auf.\n\n"
                            "`funfact`\nGibt einen zufälligen Funfact aus.\n\n"
                            "`add-funfact [FUNFACT]`\nFügt einen neuen Funfact hinzu.\n\n"
                            "`remove-funfact [ID]`\nEntfernt einen Funfact.\n\n"
                            "`hausmeister`\nÖffnet das Hausmeister-Menü.\n\n"
                }
            }
        ]
    }
