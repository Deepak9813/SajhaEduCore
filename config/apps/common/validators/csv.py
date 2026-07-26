from pathlib import Path
import csv

from django.core.exceptions import ValidationError

from apps.common.constants import MAX_CSV_SIZE

def validate_csv(file):
    """Validate uploaded CSV files."""

    if not file:
        # return file
        return

    extension = Path(file.name).suffix.lower()

    if extension != ".csv":
        raise ValidationError(
            "Only CSV files are allowed."
        )

    if file.size > MAX_CSV_SIZE:
        raise ValidationError(
            "CSV file size must not exceed 5 MB."
        )

    # Validate actual CSV content.
    # Prevents files with fake extensions (e.g., virus.exe renamed as .csv).
    try:
        decoded = file.read().decode("utf-8").splitlines()
        list(csv.reader(decoded))
        file.seek(0)  # Reset file pointer after reading

    except (UnicodeDecodeError, csv.Error):
        raise ValidationError(
            "Invalid CSV file."
        )

