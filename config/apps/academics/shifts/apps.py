from django.apps import AppConfig


class ShiftsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics.shifts'
    label = 'shifts'             #optional
    verbose_name = 'Shifts'      #optional

