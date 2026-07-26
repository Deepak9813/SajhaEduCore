import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from rest_framework import status
from rest_framework.exceptions import (
    ValidationError,
    AuthenticationFailed,
    NotAuthenticated,
    PermissionDenied,
    NotFound,
)
from rest_framework.response import Response
from rest_framework.views import exception_handler


logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
    Handle API exceptions.

    - Return a common error response format.
    - Handle validation, authentication, permission, and not found errors.
    - Log unexpected server errors.
    """

    # Let DRF handle default exceptions first
    response = exception_handler(exc, context)


    if response is not None:

        # 400 - Validation Error
        if isinstance(exc, ValidationError):
            return Response(
                {
                    "success": False,
                    "message": "Validation failed.",
                    "errors": response.data,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


        # 401 - Authentication errors
        # Example: Invalid JWT token, missing authentication
        if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
            return Response(
                {
                    "success": False,
                    "message": "Authentication failed.",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )


        # 403 - Permission Error
        # Example: User does not have required role/permission
        if isinstance(exc, PermissionDenied):
            return Response(
                {
                    "success": False,
                    "message": "Permission denied.",
                },
                status=status.HTTP_403_FORBIDDEN,
            )


        # 404 - Not Found
        # Handles both DRF NotFound and Django Http404
        if isinstance(exc, (NotFound, Http404)):
            return Response(
                {
                    "success": False,
                    "message": "Data not found.",
                },
                status=status.HTTP_404_NOT_FOUND,
            )


        # Other DRF exceptions
        # Example: Throttling, ParseError, MethodNotAllowed
        if isinstance(response.data, dict):
            message = response.data.get("detail", "Request failed.")
        else:
            message = "Request failed."
        return Response(
            {
                "success": False,
                "message": message
                # "message": response.data.get(
                    # "detail",
                    # "Request failed."
                # )
                # if isinstance(response.data, dict)
                # else "Request failed.",
            },
            status=response.status_code,
        )


    # 404-Django model DoesNotExist
    if isinstance(exc, ObjectDoesNotExist):
        return Response(
            {
                "success": False,
                "message": "Data not found.",
            },
            status=status.HTTP_404_NOT_FOUND,
        )


    # Unexpected server errors(500)
    logger.exception(exc)


    return Response(
        {
            "success": False,
            "message": "Internal server error.",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )

