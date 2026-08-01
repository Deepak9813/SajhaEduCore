from rest_framework import serializers

from apps.academics.employees.models import Employee
from apps.common.utils.strings import normalize_email
from apps.common.mixins.serializers.normalization import (
    NormalizeStringFieldsMixin
)
from apps.common.validators import (
    validate_email_domain,
    validate_nepal_mobile_number,
)


class EmployeeSerializer(NormalizeStringFieldsMixin, serializers.ModelSerializer):
    normalize_fields = [
        "full_name",
        "address",
        "designation",
    ]

    class Meta:
        model = Employee
        fields = [
            "reference_id",
            "full_name",
            "email",
            "address",
            "phone_number",
            "salary",
            "designation",
            "joined_date",
            "status"
        ]

    def validate_email(self, email):
        """
        Normalize and validate employee email address.
        """
        email = normalize_email(email)
        validate_email_domain(email)

        queryset = Employee.objects.filter(email=email, is_deleted=False)

        # Ignore current employee during update
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Email already exists.")
       
        return email
    
    def validate_phone_number(self, phone_number):
        """
        Validate employee phone number.
        """

        validate_nepal_mobile_number(phone_number)

        queryset = Employee.objects.filter(phone_number=phone_number)

        # Ignore current employee during update
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Phone number already exists.")

        return phone_number