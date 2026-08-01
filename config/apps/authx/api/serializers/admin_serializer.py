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
    phone_number = PhoneNumberField()

    password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password"
        },
        error_messages={
            "required": "Password is required."
        }
    )

    confirm_password = serializers.CharField(
        write_only=True,
        style={
            "input_type": "password"
        },
        error_messages={
            "required": "Password is required."
        }
    )

    normalize_fields = ["full_name"]

    class Meta:
        model = User
        fields = ["full_name", "email", "phone_number", "password", "confirm_password", "role"]


    def validate_email(self, email):
        """
        Normalize and validate email address.
        """
        email = normalize_email(email)
        validate_email_domain(email)

        queryset = User.objects.filter(email=email, is_deleted=False)

        # Ignore current user during update
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Email already exists.")
        
        return email
        
    def validate_phone_number(self, phone_number):
        """
        Validate phone number.
        """

        validate_nepal_mobile_number(phone_number)

        queryset = User.objects.filter(phone_number=phone_number, is_deleted=False)

        # Ignore current user during update
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Phone number already exists.")

        return phone_number

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match.")

        return data

    def validate_password(self, password):
        validate_password(password)
        return password

    
        

