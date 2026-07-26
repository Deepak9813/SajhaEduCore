from django.utils import timezone


def create_instance(model, validated_data, user=None):
    """
    Create model instance with audit fields.
    """

    return model.objects.create(
        **validated_data,
        created_by=user,
        created_at=timezone.now(),
    )