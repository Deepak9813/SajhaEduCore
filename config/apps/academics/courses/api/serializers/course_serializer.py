from django.utils import timezone
from rest_framework import serializers

from apps.academics.courses.models import Course
from apps.common.mixins.serializers.normalization import NormalizeStringFieldsMixin


class CourseSerializer(NormalizeStringFieldsMixin, serializers.ModelSerializer):
    normalize_fields = [
        "name",
        "status",
    ]

    class Meta:
        model = Course
        fields = [
            "reference_id",
            "name",
            "description",
            "duration",
            "course_fee",
            "status",
        ]
        read_only_fields = [
            "reference_id",
        ]






   