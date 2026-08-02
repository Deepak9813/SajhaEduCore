EMPLOYEE_CODE_PREFIX = "SI-EMP-"


def generate_employee_code(employee_id: int) -> str:
    """
    Generate employee code.

    Example:
        SI-EMP-000001
    """

    return f"{EMPLOYEE_CODE_PREFIX}{employee_id:06d}"