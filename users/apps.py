from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # After creating signals
    def ready(self):
        import users.signals
