from django.db import models

from apps.common.models import BaseModel

# Create your models here.
class Course(BaseModel):
    course_name = models.CharField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField()
    course_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'courses'
        # ordering = ["-id"]

    def __str__(self):
        return self.course_name
    