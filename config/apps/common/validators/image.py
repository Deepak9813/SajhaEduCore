from pathlib import Path

from django.core.exceptions import ValidationError
from PIL import Image, UnidentifiedImageError

from apps.common.constants import ALLOWED_IMAGE_EXTENSIONS, MAX_IMAGE_SIZE


def validate_image(image):
    """Validate uploaded image files."""

    if not image:
        # return image
        return

    # Validate file extension
    extension = Path(image.name).suffix.lower().lstrip(".")

    if extension not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            "Only JPG, JPEG, PNG images are allowed."
        )

    # Validate file size
    if image.size > MAX_IMAGE_SIZE:
        raise ValidationError(
            "Image size must not exceed 2 MB."
        )

    # Check actual image content
    # Prevents fake files like virus.exe renamed as image.jpg
    try:
        Image.open(image).verify()
        image.seek(0)  # Reset file pointer after verification

    except (UnidentifiedImageError, OSError):
        raise ValidationError(
            "Invalid image file."
        )
