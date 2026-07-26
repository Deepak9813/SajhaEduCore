from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.common.mixins.response import HandleResponseMixin
from apps.common.permissions import IsAdminUser, IsSuperUser


class BaseAPIView(APIView, HandleResponseMixin):
    """
    Base API view for APIs with custom authentication
    and permission rules.
    """

    pass


class BasePublicAPIView(BaseAPIView):
    """
    Base view for public APIs.
    """

    authentication_classes = []
    permission_classes = []


class BaseAdminAPIView(BaseAPIView):
    """
    Base view for admin APIs.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


class BaseSuperUserAPIView(BaseAPIView):
    """
    Base view for superuser APIs.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUser]
