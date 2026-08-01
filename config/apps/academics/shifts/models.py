from django.db import models

from apps.common.models import BaseModel


class Shift(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "shifts"
        ordering = ["start_time"]

    def __str__(self):
        return self.name