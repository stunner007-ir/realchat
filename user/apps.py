from django.apps import AppConfig


class AuthappConfig(AppConfig):
    name = 'user'

    def ready(self):
        from . import signals
