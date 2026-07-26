from .csv import validate_csv
from .document import validate_document
from .email import validate_email_domain
from .excel import validate_excel
from .file import validate_file
from .image import validate_image
from .password import validate_password
from .pdf import validate_pdf
from .phone import validate_nepal_mobile_number

#this __all__ is optional
__all__ = [
    "validate_csv",
    "validate_document",
    "validate_email_domain",
    "validate_excel",
    "validate_file",
    "validate_image",
    "validate_password",
    "validate_pdf",
    "validate_nepal_mobile_number",
]