from django.db.models import Q

from rest_framework import status
from rest_framework.exceptions import ValidationError

from apps.academics.shifts.models import Shift
from apps.academics.shifts.payloads.shift_payload import _shift_payload
from apps.common.views import BasePublicAPIView


class ShiftSearchAPIView(BasePublicAPIView):
    """
    API for searching shifts.
    """

    def get(self, request):
        keyword = request.GET.get("keyword", "").strip()

        if not keyword:
            raise ValidationError({"keyword":"Search keyword is required."})

        shifts = Shift.objects.filter(
            name__icontains=keyword,
            is_deleted=False
        ).order_by("name")
        
        return self.success_handler(
            message="Shifts retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=[_shift_payload(shift) for shift in shifts]
        )