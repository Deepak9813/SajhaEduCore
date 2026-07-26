from rest_framework import serializers

from apps.common.utils.strings import normalize_email
from apps.common.validators.email import validate_email_domain


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        write_only=True,  # Hide from API response
        error_messages={
            "required": "Email is required.",
            "blank": "Email cannot be blank.",
            "invalid": "Please enter a valid email.",
        },
    )

    password = serializers.CharField(
        write_only=True,
        trim_whitespace=False,  # Do not remove leading and trailing whitespaces
        style={"input_type": "password"},
        error_messages={
            "required": "Password is required.",
            "blank": "Password cannot be blank.",
        },
    )

    def validate_email(self, email):
        """
        Normalize and validate email address.
        """
        email = normalize_email(email)
        validate_email_domain(email)

        return email
    
