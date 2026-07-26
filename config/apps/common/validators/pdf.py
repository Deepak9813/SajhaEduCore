"""
Validator for PDF files.
"""

from pathlib import Path

from django.core.exceptions import ValidationError
from pypdf import PdfReader  #terminal: pip install pypdf

from apps.common.constants import MAX_PDF_SIZE


def validate_pdf(file):
    """Validate uploaded PDF files."""

    if not file:
        # return file
        return

    extension = Path(file.name).suffix.lower()

    if extension != ".pdf":
        raise ValidationError(
            "Only PDF files are allowed."
        )

    if file.size > MAX_PDF_SIZE:
        raise ValidationError(
            "PDF size must not exceed 10 MB."
        )

    # Validate actual pdf content.
    # Prevents files with fake extensions (e.g., virus.exe renamed as .pdf).
    try:
        PdfReader(file)
        file.seek(0)

    except Exception:
        raise ValidationError(
            "Invalid PDF file."
        )
    