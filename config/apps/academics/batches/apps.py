from django.apps import AppConfig


class BatchesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics.batches'
    label = 'batches'             #optional
    verbose_name = 'Batches'      #optional
