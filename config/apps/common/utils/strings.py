"""
String normalization utilities.
"""


def normalize_string(value: str) -> str:
    """
    Remove leading, trailing,
    and multiple spaces from string values.
    """

    if not isinstance(value, str):
        return value

    return " ".join(value.split())


def normalize_email(value: str) -> str:
    """
    Normalize email address.

    Removes surrounding spaces
    and converts email to lowercase.
    """

    if not isinstance(value, str):
        return value

    return value.strip().lower()


def normalize_username(value: str) -> str:
    """
    Normalize username.

    Removes surrounding spaces
    and converts username to lowercase.
    """

    if not isinstance(value, str):
        return value

    return value.strip().lower()


def normalize_password(value: str) -> str:
    """
    Remove leading and trailing spaces from password.
    """

    if not isinstance(value, str):
        return value

    return value.strip()

