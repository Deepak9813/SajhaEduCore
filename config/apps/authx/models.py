import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class SajhaUser(AbstractUser):
    """
    Custom user model for SajhaEduCore.

    Django Permissions:
        - is_superuser -> System owner
        - is_staff -> Institute administrator

    Application Roles:
        - Teacher
        - Employee
        - Student
    """

    class UserRole(models.TextChoices):
        ADMIN = "admin", "Admin"
        EMPLOYEE = "employee", "Employee"
        TEACHER = "teacher", "Teacher"
        STUDENT = "student", "Student"
    
    reference_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True) 
    phone_number = PhoneNumberField(unique=True, region="NP")

    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STUDENT
    )

    # is_active = models.BooleanField(default=True) #optional it is bydeafult in UserModel

    created_by = models.ForeignKey("self", on_delete=models.PROTECT, related_name="+", db_column="created_by", null=True)
    updated_by = models.ForeignKey("self", on_delete=models.PROTECT, null=True, related_name="+", db_column="updated_by")
    updated_at = models.DateField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "phone_number", "username", "role"]

    class Meta:
        db_table = 'sajha_users'
        

   




