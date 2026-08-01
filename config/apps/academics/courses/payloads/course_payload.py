def _course_payload(course):
    """
    Return course payload.
    """
      
    return {
        "id": course.id,  # "id": course.pk
        "reference_id": course.reference_id,
        "course_name": course.course_name,
        "description": course.description,
        "duration": course.duration,
        "status": course.status,
        "created_at": course.created_at.isoformat(),
        "created_by": course.created_by.id,
        
    }