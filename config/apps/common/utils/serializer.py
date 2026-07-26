from rest_framework.exceptions import ValidationError


def validate_serializer(serializer):
    """Validate the serializer and return it if valid; otherwise, raise a validation error."""
    if serializer.is_valid():
        return serializer

    raise ValidationError(serializer.errors)



'''
from rest_framework.exceptions import ValidationError


def validate_serializer(serializer):
    """
    Validate the serializer.

    Raises:
        ValidationError: If serializer validation fails.
    """
    serializer.is_valid(raise_exception=True)
    return serializer



'''