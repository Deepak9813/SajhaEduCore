from rest_framework import status
from rest_framework.response import Response


class HandleResponseMixin:
    """Mixin for handling standardized API responses."""

    def success_handler(self:object, message:str, status_code:int, data:list=None):
        response = {
            "success": True,
            "message": message,
            "data": data,
            "error": None
        }
        return Response(response, status=status_code)
    

    