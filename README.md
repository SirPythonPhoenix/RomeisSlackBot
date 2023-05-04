# RomeisSlackBot

![Slack App Icon](https://slack.com/img/product-ui-generator/apps/slackbot.png)

Ziel dieser Slack-App ist, den OnBoarding Prozess von neuen Mitarbeitenden zu verbessern und eine zentrale Anlaufstelle für Fragen und Informationen zu sein.
Die Applikation umfasst daher einige hilfreiche Slack-Commands, aber auch eine Info-Seite im Profil der Anwendung in Slack mit einem Bereich für häufig gestellte Fragen.


Hier finden Sie eine kleine Einleitung durch den ersten Prototypen unseres SlackBots der die Einleitung neuer Mitarbeitender, vor allem durch das Automatisieren der ersten Nachrichten an den neuen Mitarbeitenden, erleichtern soll.

Nun ein kurzer Überblick durch die einzelnen Dateien.

--> In der ersten Datei app.py wird der neue Mitarbeitende mit einer Willkommensnachricht willkommen geheißen, sobald er neu in den Channel gejoined ist, diese enthält unter anderem Links zu verschiedenen Seiten, die zur schnellen Einarbeitungshilfe beitragen sollen und auf die Wesentlichsten und meistgenutzen Dinge firmenintern bezogen sind.
Außerdem gibt es einen Verweis auf die wichtigsten Channels und eine Kurzbeschreibung zu diesen.

--> In der zweiten Datei commands.py sind alle bisher verwendeten Commands implementiert worden, alle Commands funktionieren mit einem "/" vor dem Command Namen und mit Eingabe eines "/" werden alle verfügbaren Commands eingeblendet.

--> In der dritten Datei HomeTab.py ist der HomeTab designed worden, dieser enthält wie auch in der Willkommensanchricht Verweise auf die wichtigsten Channels im internen Slack und verweist auf die nützlichsten Seiten/Kurse um dir den Einstieg hier zu erleichtern bzw. dient auch als Nachschlagewerk für jegliche Fragestellungen innerhalb dieser Bereiche.

--> In der vierten Datei feedback.py wird eine Woche, nachdem ein/e Mitarbeitende/r dem Slack Channel neu beigetreten ist, wird eine kleine Feedback Umfrage über die ersten Eindrücke hier in der Firma/Verbesserungsvorschläge etc. die über einen Link zu errreichen ist, verschickt.
2 Tage später soll eine kleine Abfrage gemacht werden, ob dieser Feedbackbogen bereits ausgefüllt wurde oder nicht und die/der Mitarbeitende nochmal daran erinnert werden und falls nötig der Bogen noch einmal zugesendet werden. Diese Funktion konnte ich bisher leider noch nicht vollständig einfügen, da bei mir nach Klicken des Buttons der Nachfrage keine Reaktion mehr erfolgt ist.