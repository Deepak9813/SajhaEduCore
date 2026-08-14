from rest_framework import serializers

from apps.common.utils.strings import normalize_email
from apps.common.validators.email import validate_email_domain


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        write_only=True,  # Hide from API response
        trim_whitespace=True, 
        error_messages={
            "required": "Username is required.",
            "blank": "Username cannot be blank.",
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

