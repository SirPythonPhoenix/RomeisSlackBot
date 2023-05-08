# base module import
import datetime

agreement_inputs = [
    {
        "text": {
            "type": "plain_text",
            "text": "Stimme voll zu",
            "emoji": True
        },
        "value": "5"
    },
    {
        "text": {
            "type": "plain_text",
            "text": "Stimme teilweise zu",
            "emoji": True
        },
        "value": "4"
    },
    {
        "text": {
            "type": "plain_text",
            "text": "Kann ich nicht sagen",
            "emoji": True
        },
        "value": "3"
    },
    {
        "text": {
            "type": "plain_text",
            "text": "Stimme in Teilen nicht zu",
            "emoji": True
        },
        "value": "2"
    },
    {
        "text": {
            "type": "plain_text",
            "text": "Stimme gar nicht zu",
            "emoji": True
        },
        "value": "1"
    }
]


def hausmeister(last_request):
    diff = datetime.datetime.now() - last_request if last_request else ""
    return {
        "title": {
            "type": "plain_text",
            "text": "Hausmeister-Menü",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Anfordern",
            "emoji": True
        },
        "type": "modal",
        "callback_id": "hausmeister_submit",
        "close": {
            "type": "plain_text",
            "text": "Abbrechen",
            "emoji": True
        },
        "blocks": [
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Die letzte Hausmeister-Anfrage wurde vor vor {diff.days} Tagen "
                            f"(am {last_request.day}.{last_request.month}.{last_request.year} um {last_request.hour}:{last_request.minute} Uhr) "
                            f"gesendet." if last_request else "Es wurde noch keine Anfrage an den Hausmeister getätigt."
                }
            },
            {
                "type": "input",
                "block_id": "goods",
                "element": {
                    "type": "checkboxes",
                    "options": [
                        {
                            "text": {
                                "type": "mrkdwn",
                                "text": ":coffee: Kaffee"
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "mrkdwn",
                                "text": ":soap: Seife"
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "mrkdwn",
                                "text": ":roll_of_paper: Klopapier"
                            },
                            "value": "value-2"
                        },
                        {
                            "text": {
                                "type": "mrkdwn",
                                "text": ":basket: Handtücher"
                            },
                            "value": "value-3"
                        },
                        {
                            "text": {
                                "type": "mrkdwn",
                                "text": ":lotion_bottle: Desinfektionsmittel"
                            },
                            "value": "value-4"
                        }
                    ],
                    "action_id": "checkboxes-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "Güter",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "comment",
                "label": {
                    "type": "plain_text",
                    "text": "Kommentar",
                    "emoji": True
                },
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "plain_text_input-action"
                },
                "optional": True
            },
            {
                "type": "input",
                "element": {
                    "type": "checkboxes",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Mir ist bewusst, dass durch das Drücken auf `Anfordern` unwiederruflich eine Mail an den Hausmeister gesendet wird.",
                                "emoji": True
                            },
                            "value": "value-0"
                        }
                    ],
                    "action_id": "checkboxes-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "Einwilligung",
                    "emoji": True
                }
            }
        ]
    }


def umfrage_einstellungsprozess():
    return {
        "type": "modal",
        "callback_id": "einstellungsprozess_submit",
        "title": {
            "type": "plain_text",
            "text": "Einstellungsprozess",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": True
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Dies ist eine Umfrage über unseren Einstellungsprozess. "
                            "Bitte beantworten sie alle Fragen und bestätigen sie anschließend diesen Fragebogen."
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "input",
                "block_id": "input_1",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "plain_text_input-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "1. Wer ist dein Hauptansprechpartner bei uns?",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_2",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "2. Der Einstellungsprozess war professionell.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_3",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "3. Während des Einstellungsprozess habe ich etwas über das Unternehmen "
                            "und meinen Beruf gelernt.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_4",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "plain_text_input-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "4. Haben sie Vorschläge wie wir den Einstellungsprozess verbessern können?",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_5",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "5. Die Ausrüstung oder Resourcen, die ich benötige, "
                            "standen für mich bereit, als ich meinen Job begann. "
                            "(Computer, Werkzeuge, Materialien, etc.)",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_6",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "6. Nach dem Onboarding fühle ich mich sicher im Umgang mit der "
                            "Ausrüstung und den Ressourcen, die meine Arbeit erfordert.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_7",
                "element": {
                    "type": "radio_buttons",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "ja",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "größtenteils",
                                "emoji": True
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "kann ich nicht sagen",
                                "emoji": True
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "nein",
                                "emoji": True
                            },
                            "value": "value-2"
                        }
                    ],
                    "action_id": "radio_buttons-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "7. Haben Sie das Gefühl, dass Ihnen sämtliche Ausrüstung und Ressourcen "
                            "zur Verfügung gestellt werden, die Sie benötigen, um Ihre Arbeit gut zu erledigen?",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_8",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "8. Die Informationen, die ich während des Onboardings erhielt, "
                            "waren auf dem richtigen Niveau für mich.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_9",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "9. Ich habe jetzt ein klares Verständnis davon, "
                            "was von mir in diesre Rolle erwartet wird.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_10",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "10. Ich fühle mich hier willkommen.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_11",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "11. Die Arbeit hier ist, wie ich es mir erhofft hatte.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_12",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "12. Ich habe das Gefühl, ich passe in dieses Team / Unternehmen.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_13",
                "element": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": agreement_inputs,
                    "action_id": "static_select-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "13. Ich kann mir vorstellen, dass ich in einem Jahr imer noch hier arbeite.",
                    "emoji": True
                }
            },
            {
                "type": "input",
                "block_id": "input_14",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "plain_text_input-action"
                },
                "label": {
                    "type": "plain_text",
                    "text": "14. Was können wir tun, um die Onboarding-Experience für neue Mitarbeiter zu verbessern?",
                    "emoji": True
                }
            }
        ]
    }
