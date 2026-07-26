from django.apps import AppConfig


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics.students'
    label = 'students'             #optional
    verbose_name = 'Students'      #optional
