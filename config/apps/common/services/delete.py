from django.utils import timezone


def delete_instance(instance, user=None):
    """
    Soft delete model instance with audit fields.
    """

    instance.is_deleted = True
    instance.deleted_by = user
    instance.deleted_at = timezone.now()
    instance.updated_by = user

    instance.save(
        update_fields=[
            "is_deleted",
            "deleted_by",
            "deleted_at",
            "updated_by",
        ]
    )

    return instance