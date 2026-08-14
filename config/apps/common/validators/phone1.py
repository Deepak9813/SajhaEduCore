"""
Custom phone number validators.
"""

from django.core.exceptions import ValidationError


NEPAL_MOBILE_PREFIXES = (
    "96",
    "97",
    "98",
)


def validate_nepal_mobile_number(phone):
    """
    Validate Nepal mobile numbers only.

    Accepted:
        +9779812345678
        +9779763617172

    PhoneNumberField handles:
        - format validation
        - length validation
        - invalid number detection

    This validator handles:
        - Nepal-only mobile restriction
    """

    if not phone:
        raise ValidationError(
            "Phone number is required."
        )

    phone = str(phone)

    # Remove Nepal country code
    if phone.startswith("+977"):
        phone = phone[4:]

    # Remove spaces and hyphens
    phone = phone.replace(" ", "").replace("-", "")

    if not phone.startswith(NEPAL_MOBILE_PREFIXES):
        raise ValidationError(
            "Only Nepal mobile numbers are allowed."
        )

