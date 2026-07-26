# Image upload settings
ALLOWED_IMAGE_EXTENSIONS = {
    "jpg",
    "jpeg",
    "png",
}

MAX_IMAGE_SIZE = 2 * 1024 * 1024  # 2 MB

# PDF settings
MAX_PDF_SIZE = 10 * 1024 * 1024  # 10 MB

# Document settings
MAX_DOCUMENT_SIZE = 10 * 1024 * 1024  # 10 MB

# Excel settings
MAX_EXCEL_SIZE = 10 * 1024 * 1024  # 10 MB

# CSV settings
MAX_CSV_SIZE = 5 * 1024 * 1024  # 5 MB

# File upload settings
ALLOWED_FILE_EXTENSIONS = {
    "pdf",
    "doc",
    "docx",
    "xls",
    "xlsx",
    "csv",
    "txt",
}

ALLOWED_FILE_CONTENT_TYPES = {
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "text/csv",
    "text/plain",
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# NOTE: phone number setting always include in setting