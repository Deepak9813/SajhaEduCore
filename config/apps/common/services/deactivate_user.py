from django.utils import timezone


def deactivate_user(instance, user=None):
    """
    Deactive user account model instance with audit fields.
    """

    instance.is_active = False
    instance.updated_by = user

    instance.save(
        update_fields=[
            "is_active",
            "updated_by",
        ]
    )

    return instance
