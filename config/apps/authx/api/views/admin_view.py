from django.contrib.auth import get_user_model

from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from apps.authx.api.serializers.admin_serializer import AdminSerializer
from apps.authx.services import (
    create_admin,
    create_user,
    update_user
)
from apps.common.services import delete_instance, deactivate_user
from apps.common.utils.serializer import validate_serializer
from apps.common.views import BaseSuperUserAPIView


User = get_user_model()


def _admin_payload(admin):
    """
    Return user payload.
    """
      
    return {
        "reference_id": admin.reference_id,
        "full_name": admin.full_name,
        "username": admin.username,
        "email": admin.email,
        "phone_number": str(admin.phone_number),
        "role": admin.role,
        "is_superuser": admin.is_superuser,
        "is_staff": admin.is_staff
    }


class AdminListCreateAPIView(BaseSuperUserAPIView):
    """
    API for listing and creating admins.
    """
    def get(self, request):
        # admins = User.objects.filter(is_staff=True, role="admin", is_deleted=False)
        admins = User.objects.filter(is_staff=True, role=User.UserRole.ADMIN, is_active=True)

        data = [_admin_payload(admin) for admin in admins]
        return self.success_handler(
            message="Admins retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=data
        )

    @swagger_auto_schema(
        request_body=AdminSerializer
    )
    def post(self, request):
        serializer = AdminSerializer(data=request.data, context={"request":request})
        validate_serializer(serializer)

        # user = request.user if request and request.user.is_authenticated else None
        user = request.user if request.user.is_authenticated else None

        admin = create_admin(User, serializer.validated_data, user)
        # data = _admin_payload(admin)
        return self.success_handler(
            message="Admin created successfully.",
            status_code=status.HTTP_201_CREATED,
            data=_admin_payload(admin)
        )


class AdminDetailAPIView(BaseSuperUserAPIView):
    """
    API for retrieving, updating and deleting a admin.
    """

    def _get_admin(self, reference_id):
        # return User.objects.get(reference_id=reference_id, is_staff=True, role="admin", is_deleted=False)
        return User.objects.get(
            reference_id=reference_id,
            is_staff=True,
            is_superuser=False,
            role=User.UserRole.ADMIN,
            is_deleted=False
        )
        

    def get(self, request, reference_id):
        admin = self._get_admin(reference_id)

        # data = _admin_payload(admin)
        return self.success_handler(
            message="Admin retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=_admin_payload(admin)
        )

    @swagger_auto_schema(
        request_body=AdminSerializer
    )
    def patch(self, request, reference_id):
        admin = self._get_admin(reference_id)
        serializer = AdminSerializer(admin, data=request.data, partial=True, context={"request":request})
        validate_serializer(serializer)

        user = request.user if request.user.is_authenticated else None
        admin = update_user(admin, serializer.validated_data, user)
        
        # data = _admin_payload(admin)
        return self.success_handler(
            message="Admin updated successfully.",
            status_code=status.HTTP_200_OK,
            data=_admin_payload(admin)
        )

    def delete(self, request, reference_id):
        admin = self._get_admin(reference_id)
        user = request.user if request.user.is_authenticated else None

        admin = deactivate_user(admin, user)

        # data = _admin_payload(admin)
        return self.success_handler(
            message="Admin deleted successfully.",
            status_code=status.HTTP_200_OK,
            data=_admin_payload(admin)
        )


