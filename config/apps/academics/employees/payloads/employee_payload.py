def _employee_payload(employee):
    """
    Return employee payload.
    """
    
    return {
        "reference_id": employee.reference_id,
        "employee_code": employee.employee_code,
        "full_name": employee.full_name,
        "email": employee.email,
        "phone_number": str(employee.phone_number),
        "address": employee.address,
        "designation": employee.designation,
        "joined_date": employee.joined_date.isoformat(),
        "status": employee.status,
    }