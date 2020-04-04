from django.apps import AppConfig

from data_getter import updater


class StatesConfig(AppConfig):
    name = 'states'

    def ready(self):
        updater.start()
