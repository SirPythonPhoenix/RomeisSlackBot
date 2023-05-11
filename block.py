from views import umfrage_einstellungsprozess


def feedback_bogen(user_id):
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Feedback-Bogen",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"<@{user_id}> Du bist bereits seit einer Woche bei uns! \n"
                        f"Um unseren Einstellungsprozess fortlaufend verbessern zu können, "
                        f"freuen wir uns über dein Feedback.\n"
                        f"Wir möchten dich deshalb bitten, an unserem Feedback-Bogen teilzunehmen."
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Zum Feedback-Bogen",
                        "emoji": True
                    },
                    "value": "click_me",
                    "action_id": "einstellungsprozess_oeffnen"
                }
            ]
        }
    ]


def welcome(user_id):
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Willkommen zum Team! 🎉",
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"<@{user_id}> Wir freuen uns, dass Du den Weg hierher gefunden hast und hoffen, "
                        "dass Du dich gut zurechtfindest."
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Hier findest Du diverse weitere Links die Dir den Einstieg erleichtern sollen "
                        "und eine Einleitung der wichtigsten Channels. ",
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Nutze `/hilfe` um eine Übersicht der Bot-Befehle zu erhalten.",
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Linksammlung",
            }
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
                "type": "mrkdwn",
                "text": "Basic Git Kurs"
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
                "type": "mrkdwn",
                "text": "PHP 8.0"
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Zur Webseite",
                },
                "value": "click_me_123",
                "url": "https://phptherightway.com/",
                "action_id": "button-action"
            }
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
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Channels",
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*#team-programming -->* für gemeinsame Coding Sessions"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*#general -->* Hier gibt's allgemeine betriebliche Informationen"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*#triangulum-mittag -->* Hier wird abgestimmt fürs Mittagessen"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*#kudos -->* Hier kannst Du deine Kollegen für herausragende Leistungen loben"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*#slackoverflow -->* Ist unser internes Stackoverflow "
            }
        },
        {
            "type": "divider"
        }
    ]


def feedback_results(user_name, values):
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Ergebnisse des Feedbackbogens von {user_name}",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][2]['label']['text']}* \n"
                        f"_{values['input_1']['plain_text_input-action']['value']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][3]['label']['text']}* \n"
                        f"_{values['input_2']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][4]['label']['text']}* \n"
                        f"_{values['input_3']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][5]['label']['text']}* \n"
                        f"_{values['input_4']['plain_text_input-action']['value']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][6]['label']['text']}* \n"
                        f"_{values['input_5']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][7]['label']['text']}* \n"
                        f"_{values['input_6']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][8]['label']['text']}* \n"
                        f"_{values['input_7']['radio_buttons-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][9]['label']['text']}* \n"
                        f"_{values['input_8']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][10]['label']['text']}* \n"
                        f"_{values['input_9']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][11]['label']['text']}* \n"
                        f"_{values['input_10']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][12]['label']['text']}* \n"
                        f"_{values['input_11']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][13]['label']['text']}* \n"
                        f"_{values['input_12']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][14]['label']['text']}* \n"
                        f"_{values['input_13']['static_select-action']['selected_option']['text']['text']}_"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*{umfrage_einstellungsprozess()['blocks'][15]['label']['text']}* \n"
                        f"_{values['input_14']['plain_text_input-action']['value']}_"
            }
        },

    ]


def roulette_intro(participiants):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Die Teilnahme am Kuchen-Rolette vergütet dich jeden Monat mit einem Kuchen... "
                        f"der einzige Haken? - du musst ihn das ein oder andere Mal selber backen. \n"
                        f"Drücke auf `Teilnehmen`, um teilzunehmen. \n"
                        f"Zurzeit nehmen {len(participiants)} Personen teil."
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Teilnehmen"
                    },
                    "style": "primary",
                    "value": "some_value",
                    "action_id": "roulette_participate"
                }
            ]
        }
    ]


def roulette_participiant(participiants):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Du bist zurzeit einer von {len(participiants)} glücklichen Teilnehmern des Kuchen-Roulettes."
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "emoji": True,
                        "text": "Nicht mehr teilnehmen"
                    },
                    "style": "danger",
                    "value": "some_value",
                    "action_id": "roulette_leave"
                }
            ]
        }
    ]
