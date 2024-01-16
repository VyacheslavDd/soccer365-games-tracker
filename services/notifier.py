from win10toast import ToastNotifier
import os
import common.constants as constants

class Notifier:
    __notifier = ToastNotifier()

    @classmethod
    def notify(cls, title, message):
        try:
            cls.__notifier.show_toast(title=title, msg=message, duration=constants.NOTIFICATION_TIMEOUT_TIME,
                            icon_path=os.path.join("graphic_data", "icons", "soccer_icon.ico"))
        except Exception as exc:
            print(exc)
            try:
                cls.__notifier.show_toast(title=title, msg=message, duration=constants.NOTIFICATION_TIMEOUT_TIME,
                                    icon_path=os.path.join("_internal", "graphic_data", "icons", "soccer_icon.ico"))
            except Exception as exc:
                print(exc)
                cls.__notifier.show_toast(title=title, msg=message, duration=constants.NOTIFICATION_TIMEOUT_TIME)

    @classmethod
    def do_notifications_for_game(cls, game, score, status, details):
        if game.status != status and not (game.status.startswith("Идёт") and status.startswith("Идёт")):
            cls.notify(f"{game.title}, {score}", f"Изменился статус матча: {status}")
        if len(game.details) < len(details):
            new_details = details[len(game.details):]
            for detail in new_details:
                cls.notify(f"{game.title}, {score}", detail)
        if game.score != score:
            cls.notify(f"{game.title}, {score}", "Изменился счёт матча!")
