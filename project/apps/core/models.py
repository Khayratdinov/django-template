import uuid
from django.db import models


class TimeStampedModel(models.Model):
    """
    Model that provides self-updating 'created' and 'updated' fields for tracking records.
    """

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Time when this record was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Time when this record was last updated."
    )

    class Meta:
        abstract = True
        ordering = ["-created_at"]  # Default ordering by the newest records first.

    def __str__(self):
        return f"Record created on {self.created_at} and updated on {self.updated_at}"


# ============================================================================ #


class UUIDModel(models.Model):
    """
    Abstract model that provides a UUID as the primary key for other models.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


# ============================================================================ #


class BaseModel(UUIDModel, TimeStampedModel):
    """
    Abstract model that provides a UUID as the primary key for other models.
    """

    class Meta:
        abstract = True
