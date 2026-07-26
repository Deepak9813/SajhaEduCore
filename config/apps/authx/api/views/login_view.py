from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from apps.authx.api.serializers import LoginSerializer
from apps.authx.services.tokens import generate_tokens
from apps.common.utils.serializer import validate_serializer
from apps.common.views import BasePublicAPIView


def _user_payload(user):
    """
    Return user payload.
    """
      
    return {
        "id": user.id,
        "reference_id": user.reference_id,
        "full_name": user.full_name,
        "username": user.username,
        "email": user.email,
        "phone_number": str(user.phone_number),
        "role": user.role,
        "is_superuser":user.is_superuser,
        "is_staff":user.is_staff
    }


class LoginApiView(BasePublicAPIView):
    """
    Authenticate user and generate JWT tokens.

    Returns:
        - Access token in the response body.
        - Refresh token in an HttpOnly cookie.
    """

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        validate_serializer(serializer)

        #receive validated email and password from serializer
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        
        if user is None:
            raise AuthenticationFailed("Invalid email or password.")
        
        # Generate JWT tokens
        tokens = generate_tokens(user)

        #Prepare response payload(response_data).
        data = {
            "access": tokens["access"],
            "user": _user_payload(user)
        }

        # response = self.success_handler("Login successful.", 200, data)
        response = self.success_handler("Login successful.", status.HTTP_200_OK, data)

        #set refresh token in cookie
        response.set_cookie(
            key="refresh_token",
            value=tokens["refresh"],
            httponly=True, 
            secure=False,  # True in production(HTTPS)
            samesite="Lax", 
            path="/",
            max_age=60 * 60 * 24 * 7
        )
        return response
        

        
        
            
        
