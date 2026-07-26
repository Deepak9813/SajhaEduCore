"""
Validator for Word documents (DOC/DOCX).
"""
from pathlib import Path

from django.core.exceptions import ValidationError
from docx import Document  # pip install python-docx

from apps.common.constants import MAX_DOCUMENT_SIZE


ALLOWED_DOCUMENT_EXTENSIONS = {
    ".doc",
    ".docx",
}


def validate_document(file):
    """Validate uploaded Word documents."""

    if not file:
        # return file
        return

    extension = Path(file.name).suffix.lower()

    if extension not in ALLOWED_DOCUMENT_EXTENSIONS:
        raise ValidationError(
            "Only DOC and DOCX files are allowed."
        )

    if file.size > MAX_DOCUMENT_SIZE:
        raise ValidationError(
            "Document size must not exceed 10 MB."
        )

    # Validate actual DOCX content.
    # Prevents files with fake extensions (e.g., virus.exe renamed as .docx).
    if extension == ".docx":
        try:
            Document(file)
            file.seek(0)

        except Exception:
            raise ValidationError(
                "Invalid DOCX file."
            )
    

    # .doc files are not verified because python-docx
    # only supports .docx.