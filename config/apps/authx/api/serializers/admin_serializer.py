from django.contrib.auth import get_user_model

from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from apps.common.mixins.serializers.normalization import (
    NormalizeStringFieldsMixin,
)
from apps.common.utils.strings import normalize_email
from apps.common.validators import (
    validate_email_domain,
    validate_nepal_mobile_number,
    validate_password,
)

User = get_user_model()


class AdminSerializer(NormalizeStringFieldsMixin, serializers.ModelSerializer):
    phone_number = PhoneNumberField(region="NP")

    confirm_password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password"
        },
        error_messages={
            "required": "Password is required."
        }
    )

    normalize_fields = ["full_name", "username"]

    class Meta:
        model = User
        fields = ["full_name", "username", "email", "phone_number", "password", "confirm_password"]

        extra_kwargs = {
            "full_name": {
                "error_messages": {
                    "required": "Full name is required.",
                    "blank": "Full name cannot be blank.",
                },
            },
            "username": {
                "error_messages": {
                    "required": "Username is required.",
                    "blank": "Username cannot be blank.",
                },
            },
            "email": {
                "error_messages": {
                    "required": "Email is required.",
                    "blank": "Email cannot be blank.",
                    "invalid": "Enter a valid email address.",
                },
            },
            "phone_number": {
                "error_messages": {
                    "required": "Phone number is required.",
                    "blank": "Phone number cannot be blank.",
                    "invalid": "Enter a valid phone number.",
                },
            },
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password",
                },
                "error_messages": {
                    "required": "Password is required.",
                    "blank": "Password cannot be blank.",
                },
            },
            "role": {
                "error_messages": {
                    "required": "Role is required.",
                    "invalid_choice": "Invalid role.",
                },
            },
        }


    def validate_username(self, username):
            """
            Validate username.
            """

            queryset = User.objects.filter(username=username)
    
            # Ignore current user during update
            if self.instance:
                queryset = queryset.exclude(pk=self.instance.pk)
    
            if queryset.exists():
                raise serializers.ValidationError("Username already exists.")
            
            return username

    def validate_email(self, email):
        """
        Normalize and validate email address.
        """
        email = normalize_email(email)
        validate_email_domain(email)        
        return email
        
    def validate_phone_number(self, phone_number):
        """
        Validate phone number.
        """

        validate_nepal_mobile_number(phone_number)
        return phone_number

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def validate_password(self, password):
        validate_password(password)
        return password

