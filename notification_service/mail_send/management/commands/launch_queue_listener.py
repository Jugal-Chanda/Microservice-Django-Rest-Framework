from django.core.management.base import BaseCommand
from queue_listeners.user_created_listener import UserCreatedListener


class Command(BaseCommand):
    help = 'Launches Listener for user_created message : RaabitMQ'

    def handle(self, *args, **options):
        td = UserCreatedListener()
        td.start()
        self.stdout.write("Started Consumer Thread")
