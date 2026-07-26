from django.apps import AppConfig


class TeachersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics.teachers'
    label = 'teachers'             #optional
    verbose_name = 'Teachers'      #optional

