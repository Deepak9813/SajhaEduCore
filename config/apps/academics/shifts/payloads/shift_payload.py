def _shift_payload(shift):
    """
    Return shift payload.
    """

    return {
        "reference_id": shift.reference_id,
        "name": shift.name,
        "start_time": shift.start_time.isoformat(),
        "end_time": shift.end_time.isoformat(),
        "status": shift.status,
    }