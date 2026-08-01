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

    def validate_course_name(self, course_name):
        """
        Validate course name uniqueness.
        """

        queryset = Course.objects.filter(course_name=course_name, is_deleted=False)

        # Ignore current course during update
        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "Course name already exists."
            )

        return course_name






   