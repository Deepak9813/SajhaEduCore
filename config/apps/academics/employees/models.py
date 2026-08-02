from django.contrib.auth import get_user_model
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel

User = get_user_model()


class Employee(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name="employee",
        null=True,
        blank=True,
    )
    employee_code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(unique=True, region="NP")
    address = models.TextField()
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    designation = models.CharField(max_length=200)
    joined_date = models.DateField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "employees"
        ordering = ["-id"]

    def __str__(self):
        return self.full_name        
