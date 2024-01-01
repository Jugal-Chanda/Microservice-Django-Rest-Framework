from django.apps import AppConfig
from .queue_listeners.user_created_listener import UserCreatedListener


class MailSendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail_send'

    def ready(self) -> None:
        user_created_consumer = UserCreatedListener()
        user_created_consumer.daemon = True
        user_created_consumer.start()
        return super().ready()
