from django.db.models import Q

from rest_framework import status
from rest_framework.exceptions import ValidationError

from apps.academics.courses.models import Course
from apps.academics.courses.payloads.course_payload import _course_payload
from apps.common.views import BasePublicAPIView


class CourseSearchAPIView(BasePublicAPIView):
    """
    API for searching courses.
    """

    def get(self, request):
        keyword = request.GET.get("keyword", "").strip()

        if not keyword:
            raise ValidationError({"keyword":"Search keyword is required."})

        courses = (
            Course.objects.filter(is_deleted=False)
            .filter(
                Q(course_name__icontains=keyword)
                | Q(description__icontains=keyword)
            )
            .order_by("course_name")
        )
        # data = [_course_payload(course) for course in courses]
        return self.success_handler(
            message="Courses retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=[_course_payload(course) for course in courses]
        )