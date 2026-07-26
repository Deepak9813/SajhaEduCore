"""
Custom email validators for additional email rules.

Use only for domain restrictions or other custom checks.
For normal email validation, use serializers.EmailField().
"""


from django.core.exceptions import ValidationError


ALLOWED_EMAIL_DOMAINS = {
    "gmail.com",
    "yahoo.com",
}


def validate_email_domain(email):
    """
    Validate allowed email domains.
    """

    domain = email.split("@")[-1].lower()

    if domain not in ALLOWED_EMAIL_DOMAINS:
        raise ValidationError(
            "Only Gmail and Yahoo email addresses are allowed."
        )

