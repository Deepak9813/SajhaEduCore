"""
Serializer string normalization mixins.
"""

from apps.common.utils.strings import normalize_string


class NormalizeStringFieldsMixin:
    """
   Normalize selected string fields before validation.
    """

    normalize_fields = []

    def validate(self, attrs):
        """
         Remove extra spaces from configured (selected) string fields.
        """

        for field in self.normalize_fields:
            value = attrs.get(field)

            if isinstance(value, str):
                attrs[field] = normalize_string(value)

        return super().validate(attrs)
    
