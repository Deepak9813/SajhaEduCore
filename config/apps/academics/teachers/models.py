from django.db import models

from apps.academics.employees.models import Employee
from apps.common.models import BaseModel


class Teacher(BaseModel):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.PROTECT,
        related_name="teacher"
    )
    qualification = models.CharField(max_length=200)
    experience_year = models.PositiveIntegerField(default=0)
    specialization = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return self.employee.full_name

