from django.apps import AppConfig


class HoodAppConfig(AppConfig):
    name = 'hood_app'

    def ready(self):
        '''
        function tha registers a signal
        '''
        import hood_app.signals

