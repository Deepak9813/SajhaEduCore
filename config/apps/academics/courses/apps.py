from django.apps import AppConfig


class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics.courses'
    label = 'courses'             #optional
    verbose_name = 'Courses'      #optional

