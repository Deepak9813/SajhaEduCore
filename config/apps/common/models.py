import uuid

from django.conf import settings
from django.db import models


class BaseModel(models.Model):
    """Abstract base model with common fields."""

    reference_id = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="+",  # Disable reverse relationship.
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="+",
        null=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_deleted = models.BooleanField(default=False)

    deleted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="+",
        null=True,
        blank=True,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True