from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()


def create_admin(model, validated_data, user=None):
    """
    Create admin  with hashed password.
    """

    password = validated_data.pop("password", None)
    validated_data.pop("confirm_password", None)

    instance = model(
        **validated_data,
        is_staff=True,
        is_superuser=False,
        role=User.UserRole.ADMIN,
        created_by=user,
        created_at=timezone.now(),
    )

    if password:
        instance.set_password(password)

    instance.save()

    return instance


def create_user(model, validated_data, user=None):
    """
    Create user instance with hashed password.
    """

    password = validated_data.pop("password", None)
    validated_data.pop("confirm_password", None)

    instance = model(
        **validated_data,
        created_by=user,
        created_at=timezone.now(),
    )

    if password:
        instance.set_password(password)

    instance.save()

    return instance


def update_user(instance, data, user):
    """
    Update user instance and handle password hashing.
    """

    password = data.pop("password", None)
    data.pop("confirm_password", None)  #remove confirm password before setting field

    for field, value in data.items():
        setattr(instance, field, value)

    if password:
        instance.set_password(password)

    instance.updated_by = user
    instance.save()

    return instance