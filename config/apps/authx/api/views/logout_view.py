from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.authx.services.tokens import blacklist_refresh_token
from apps.common.views import BaseAPIView



class LogoutAPIView(BaseAPIView):
    """
    Logout user.

    - Get refresh token from HttpOnly cookie.
    - Blacklist refresh token.
    - Remove refresh token cookie.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # print("request.COOKIES =", request.COOKIES)
        # print("Cookie header =", request.headers.get("Cookie"))
        # print("======================== Hello rohit is hitting ===================")
        # receive refresh token from cookie
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            # raise ValidationError("Refresh token is required.")
            raise ValidationError(
                {"refresh_token": "Refresh token is required."}
            )

        # blacklist the token
        blacklist_refresh_token(refresh_token)
        print(request)
        response = self.success_handler("Logout successfully.", status.HTTP_200_OK)

        # delete the stored cookie safely
        # Note: do not include httponly , secure inside delete_cookie()
        response.delete_cookie(
            key="refresh_token",
            path="/",
            samesite="Lax",
        )

        return response

