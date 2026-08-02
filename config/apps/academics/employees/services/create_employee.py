from django.db import transaction

from apps.academics.employees.models import Employee
from apps.academics.employees.services.employee_code import (
    generate_employee_code,
)


@transaction.atomic
def create_employee(validated_data, user):
    """
    Create employee and generate employee code.
    """

    employee = Employee.objects.create(
        **validated_data,
        created_by=user,
        updated_by=user,
    )

    employee.employee_code = generate_employee_code(employee.id)

    employee.save(update_fields=["employee_code"])

    return employee