from rest_framework import serializers

from apps.academics.shifts.models import Shift
from apps.common.utils.strings import normalize_string


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
        fields = ["name", "start_time", "end_time", "status"]


    def validate_name(self, name):
        """
        Normalize shift name and check uniqueness.
        """
        name = normalize_string(name)

        queryset = Shift.objects.filter(name=name, is_deleted=False)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError("Shift name already exists.")
        
        return name

    def validate(self, data):
        """
        Validate that end time is after start time.
        """
        start_time = data.get("start_time")
        end_time = data.get("end_time")

        if self.instance:
            # Use the incoming value; otherwise, use the existing database value.
            start_time = start_time or self.instance.start_time
            end_time = end_time or self.instance.end_time

        if end_time <= start_time:
            raise serializers.ValidationError(
                {"end_time": "End time must be after start time."}
            )

        return data


# NOTE: if we only use PUT method in view then this lengthy validation is not required we directly:-
"""
    def validate(self, data):
        if data["end_time"] <= data["start_time"]:
            raise serializers.ValidationError(
                {"end_time": "End time must be after start time."}
            )

        return data
"""

    