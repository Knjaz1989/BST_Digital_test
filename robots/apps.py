from django.apps import AppConfig
from django.db.models.signals import post_save


class RobotsConfig(AppConfig):
    name = 'robots'
    
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals

        # Explicitly connect a signal handler.
        post_save.connect(signals.send_email_notification)
