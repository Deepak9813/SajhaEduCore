from django.apps import AppConfig


class EmployeesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.academics.employees'
    label = 'employees'             #optional
    verbose_name = 'Employees'      #optional

