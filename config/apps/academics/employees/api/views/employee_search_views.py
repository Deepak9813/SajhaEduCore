from django.db.models import Q

from rest_framework import status
from rest_framework.exceptions import ValidationError

from apps.academics.employees.models import Employee
from apps.academics.employees.payloads.employee_payload import (
    _employee_payload,
)
from apps.common.views import BasePublicAPIView


class EmployeeSearchAPIView(BasePublicAPIView):
    """
    API for searching employees.
    """

    def get(self, request):
        keyword = request.GET.get("keyword", "").strip()

        if not keyword:
            raise ValidationError({"keyword": "Search keyword is required."})

        employees = (
            Employee.objects.filter(is_deleted=False)
            .filter(
                Q(full_name__icontains=keyword)
                | Q(email__icontains=keyword)
                | Q(phone_number__icontains=keyword)
                | Q(designation__icontains=keyword)
            )
            .order_by("full_name")
        )

        # data = [_employee_payload(employee) for employee in employees]
        return self.success_handler(
            message="Employees retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=[_employee_payload(employee) for employee in employees]
        )
