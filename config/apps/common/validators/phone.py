"""
Custom phone number validators.
"""

from django.core.exceptions import ValidationError


NEPAL_COUNTRY_CODE = 977

NEPAL_MOBILE_PREFIXES = (
    "96",
    "97",
    "98",
)


def validate_nepal_mobile_number(phone):
    """
    Validate Nepal mobile numbers only.

    PhoneNumberField handles:
        - Phone number parsing
        - General format validation
        - Length validation
        - Invalid number detection

    This validator handles:
        - Nepal-only restriction
        - Nepal mobile number prefixes
    """

    if phone.country_code != NEPAL_COUNTRY_CODE:
        raise ValidationError(
            "Only Nepal mobile numbers are allowed."
        )

    national_number = str(phone.national_number)

    if not national_number.startswith(NEPAL_MOBILE_PREFIXES):
        raise ValidationError(
            "Only Nepal mobile numbers are allowed."
        )