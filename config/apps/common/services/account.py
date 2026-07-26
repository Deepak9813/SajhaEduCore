"""
User account creation services.
"""

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.exceptions import ValidationError

from apps.common.utils.generators import generate_password


User = get_user_model()


@transaction.atomic
def create_user_account(instance, role):
    """
    Create a user account and link it to the given model instance.

    Supported models:
        - Student
        - Teacher
        - Staff
    """

    if instance.user:
        raise ValidationError(
            "User account already exists."
        )

    password = generate_password()

    user = User.objects.create_user(
        username=instance.username,
        email=instance.email,
        password=password,
        role=role,
    )

    instance.user = user
    instance.status = "APPROVED"

    instance.save(
        update_fields=[
            "user",
            "status",
        ]
    )

    return {
        "user": user,
        "username": user.username,
        "password": password,
    }



"""
#======================== How to use in view ==========================
#for student
from apps.common.services.account import create_user_account

...

def post(self, request, reference_id):
    student = self._get_student(reference_id)

    account = create_user_account(
        student,
        User.Role.STUDENT,  #or direct send "STUDENT"  #NOTE: User.Role.STUDENT==> MainClass.InnerClass.VariableName
    )

    return self.success_handler(
        "Student account created successfully.",
        201,
        account,
    )

.......
# for teacher
def post(self, request, reference_id):
    teacher = self._get_teacher(reference_id)

    account = create_user_account(
        teacher,
        User.Role.TEACHER,   #or direct send "TEACHER"
    )

    return self.success_handler(
        "Teacher account created successfully.",
        201,
        account,
    )

......
# for staff
def post(self, request, reference_id):
    staff = self._get_staff(reference_id)

    account = create_user_account(
        staff,
        User.Role.STAFF,
    )

    return self.success_handler(
        "Staff account created successfully.",
        201,
        account,
    )

    

#3 urls:
POST /api/students/<reference_id>/create-account/
POST /api/teachers/<reference_id>/create-account/
POST /api/staffs/<reference_id>/create-account/

"""