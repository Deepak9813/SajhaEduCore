"""
Common value generators.
"""

import secrets
import string


def generate_password(length: int = 12) -> str:
    """
    Generate a secure random password.

    Example:
        Ab9@kL23#xPq
    """

    characters = (
        string.ascii_letters
        + string.digits
        + "@#$%&*"
    )

    return "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

