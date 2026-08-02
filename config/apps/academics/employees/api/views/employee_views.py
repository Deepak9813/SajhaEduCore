from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema

from apps.academics.employees.api.permissions import IsAdminOrReadOnly
from apps.academics.employees.api.serializers.employee_serializer import (
    EmployeeSerializer,
)
from apps.academics.employees.models import Employee
from apps.academics.employees.payloads.employee_payload import (
    _employee_payload,
)
from apps.academics.employees.services.create_employee import create_employee
from apps.common.services import (
    delete_instance,
    update_instance,
)
from apps.common.utils.serializer import validate_serializer
from apps.common.views import BaseAPIView


class EmployeeListCreateAPIView(BaseAPIView):
    """
    API for listing and creating employees.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        employees = Employee.objects.filter(is_deleted=False).order_by("-id")

        # data = [_employee_payload(employee) for employee in employees]
        return self.success_handler(
            message="Employees retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=[_employee_payload(employee) for employee in employees]
        )

    @swagger_auto_schema(
        request_body=EmployeeSerializer
    )
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data, context={"request": request})
        validate_serializer(serializer)

        user = request.user if request.user.is_authenticated else None

        employee = create_employee(serializer.validated_data, user)

        # data = _employee_payload(employee)
        return self.success_handler(
            message="Employee created successfully.",
            status_code=status.HTTP_201_CREATED,
            data=_employee_payload(employee)
        )


class EmployeeDetailAPIView(BaseAPIView):
    """
    API for retrieving, updating and deleting an employee.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def _get_employee(self, reference_id):
        return Employee.objects.get(reference_id=reference_id, is_deleted=False)

    def get(self, request, reference_id):
        employee = self._get_employee(reference_id)
        # data = _employee_payload(employee)
        return self.success_handler(
            message="Employee retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=_employee_payload(employee)
        )
    @swagger_auto_schema(
        request_body=EmployeeSerializer
    )
    def patch(self, request, reference_id):
        employee = self._get_employee(reference_id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True, context={"request":request})
        validate_serializer(serializer)

        user = request.user if request.user.is_authenticated else None

        employee = update_instance(employee, serializer.validated_data, user=user)

        # data = _employee_payload(employee)
        return self.success_handler(
            message="Employee updated successfully.",
            status_code=status.HTTP_200_OK,
            data=_employee_payload(employee)
        )

    def delete(self, request, reference_id):
        employee = self._get_employee(reference_id)
        user = request.user if request.user.is_authenticated else None

        employee = delete_instance(employee, user)
        # data = _employee_payload(employee)
        return self.success_handler(
            message="Employee deleted successfully.",
            status_code=status.HTTP_200_OK,
            data=_employee_payload(employee)
        )