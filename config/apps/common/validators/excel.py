"""
Validator for Excel files (XLS/XLSX).
"""
from pathlib import Path

from django.core.exceptions import ValidationError
from openpyxl import load_workbook  # pip install openpyxl

from apps.common.constants import MAX_EXCEL_SIZE


ALLOWED_EXCEL_EXTENSIONS = {
    ".xls",
    ".xlsx",
}


def validate_excel(file):
    """Validate uploaded Excel files."""

    if not file:
        # return file
        return

    extension = Path(file.name).suffix.lower()

    if extension not in ALLOWED_EXCEL_EXTENSIONS:
        raise ValidationError(
            "Only XLS and XLSX files are allowed."
        )

    if file.size > MAX_EXCEL_SIZE:
        raise ValidationError(
            "Excel file size must not exceed 10 MB."
        )

    # Validate actual Excel content.
    # Prevents files with fake extensions (e.g., virus.exe renamed as .xlsx).
    if extension == ".xlsx":
        try:
            load_workbook(file,  read_only=True)
            file.seek(0)    # Reset file pointer after reading

        except Exception:
            raise ValidationError(
                "Invalid XLSX file."
            )

    # .xls files require different libraries, so
    # only the extension and size are checked here.