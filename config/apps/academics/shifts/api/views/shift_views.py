from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema

from apps.academics.shifts.api.permissions import IsAdminOrReadOnly
from apps.academics.shifts.api.serializers.shift_serializer import (
    ShiftSerializer,
)
from apps.academics.shifts.models import Shift
from apps.academics.shifts.payloads.shift_payload import _shift_payload
from apps.common.services import (
    create_instance,
    delete_instance,
    update_instance,
)
from apps.common.utils.serializer import validate_serializer
from apps.common.views import BaseAPIView


class ShiftListCreateAPIView(BaseAPIView):
    """
    API for listing and creating shifts.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        shifts = Shift.objects.filter(is_deleted=False).order_by("name")
        return self.success_handler(
            message="Shifts retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=[_shift_payload(shift) for shift in shifts]
        )
    @swagger_auto_schema(
        request_body=ShiftSerializer
    )
    def post(self, request):
        serializer = ShiftSerializer(data=request.data)
        validate_serializer(serializer)

        user = request.user if request.user.is_authenticated else None

        shift = create_instance(Shift, serializer.validated_data, user)
        return self.success_handler(
            message="Shift created successfully.",
            status_code=status.HTTP_201_CREATED,
            data=_shift_payload(shift)
        )


class ShiftDetailAPIView(BaseAPIView):
    """
    API for retrieving, updating and deleting a shift.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def _get_shift(self, reference_id):
        return Shift.objects.get(reference_id=reference_id, is_deleted=False)

    def get(self, request, reference_id):
        shift = self._get_shift(reference_id)
        return self.success_handler(
            message="Shift retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=_shift_payload(shift)
        )

    @swagger_auto_schema(
        request_body=ShiftSerializer
    )
    def patch(self, request, reference_id):
        shift = self._get_shift(reference_id)
        serializer = ShiftSerializer(shift, data=request.data, partial=True)
        validate_serializer(serializer)

        user = request.user if request.user.is_authenticated else None

        shift = update_instance(shift, serializer.validated_data, user)
        return self.success_handler(
            message="Shift updated successfully.",
            status_code=status.HTTP_200_OK,
            data=_shift_payload(shift)
        )

    def delete(self, request, reference_id):
        shift = self._get_shift(reference_id)
        user = request.user if request.user.is_authenticated else None
        shift = delete_instance(shift, user)
        return self.success_handler(
            message="Shift deleted successfully.",
            status_code=status.HTTP_200_OK,
            data=_shift_payload(shift)
        )   