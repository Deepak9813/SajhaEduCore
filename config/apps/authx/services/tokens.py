from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError

def generate_tokens(user):
   if not user.is_active:
      raise AuthenticationFailed("User is not active")

   refresh = RefreshToken.for_user(user)

   return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
   }


def blacklist_refresh_token(refresh_token):
   """
   Blacklist a refresh token.
   """
   try:
      RefreshToken(refresh_token).blacklist()
   except TokenError:
      # raise ValidationError("Invalid or expired refresh token.")
      raise ValidationError( 
        {"refresh_token": ["Invalid or expired refresh token."]}
      )
      
