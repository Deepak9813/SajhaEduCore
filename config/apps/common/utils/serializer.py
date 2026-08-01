from rest_framework.exceptions import ValidationError


def validate_serializer(serializer):
    """
    Validate serializer and raise validation error if invalid.
    """
    if not serializer.is_valid():
        raise ValidationError(serializer.errors)
