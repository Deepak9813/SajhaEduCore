from django.utils import timezone

def update_instance(instance, validated_data, user=None):
    """
    Update model instance with audit fields.
    """

    for attr, value in validated_data.items():
        setattr(instance, attr, value)

    instance.updated_by = user
    instance.updated_at = timezone.now()

    instance.save()

    return instance