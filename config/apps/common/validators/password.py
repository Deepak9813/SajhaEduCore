import re

from django.core.exceptions import ValidationError


def validate_password(password):
    """
    Validate password strength.

    Requirements:
    - Minimum 8 characters
    - One uppercase letter
    - One lowercase letter
    - One digit
    - One special character
    """

    if len(password) < 8:
        raise ValidationError(
            "Password must be at least 8 characters."
        )

    if not re.search(r'[A-Z]', password):
        raise ValidationError(
            "Password must contain at least one capital letter."
        )

    if not re.search(r'[a-z]', password):
        raise  ValidationError(
            "Password must contain at least one small letter."
        ) 

    if not re.search(r'\d', password):
        raise ValidationError(
            "Password must contain at least one digit."
        )

    if not re.search(r'[\W_]', password):
        raise ValidationError(
            "Password must contain at least one special character."
        )
    
    
