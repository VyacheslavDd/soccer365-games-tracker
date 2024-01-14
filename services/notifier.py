from plyer import notification
import os
import common.constants as constants

class Notifier:
    @classmethod
    def notify(cls, title, message):
        notification.notify(title=title, message=message, timeout=constants.NOTIFICATION_TIMEOUT_TIME,
                            app_icon=os.path.join("graphic_data", "icons", "soccer_icon.ico"))
    
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
