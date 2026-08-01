from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema

from apps.academics.courses.api.permissions import IsAdminOrReadOnly
from apps.academics.courses.api.serializers.course_serializer import (
    CourseSerializer,
)
from apps.academics.courses.models import Course
from apps.academics.courses.payloads.course_payload import _course_payload
from apps.common.services.create import create_instance
from apps.common.services.update import update_instance
from apps.common.services.delete import delete_instance
from apps.common.utils.serializer import validate_serializer
from apps.common.views import BaseAPIView



class CourseListCreateAPIView(BaseAPIView):
    """
    API for listing and creating courses.
    """
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        courses = Course.objects.filter(is_deleted=False).order_by("-id")

        data = [_course_payload(course) for course in courses]  # list comprehension

        return self.success_handler(
            message="Courses retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=data
        )

    @swagger_auto_schema(
        request_body=CourseSerializer
    )
    def post(self, request):
        serializer = CourseSerializer(data=request.data, context={"request": request})
        validate_serializer(serializer)

        user = request.user if request.user.is_authenticated else None

        course = create_instance(Course, serializer.validated_data,user)

        # data = _course_payload(course)
        return self.success_handler(
            message="Course created successfully.",
            status_code=status.HTTP_201_CREATED,
            data=_course_payload(course)
        )


class CourseDetailAPIView(BaseAPIView):
    """
    API for retrieving, updating and deleting a course.
    """

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    # def _get_course(self, reference_id):      #also write request here
    #     try:
    #         return Course.objects.get(reference_id=reference_id, is_delete=False)
    #         # return Course.objects.get(reference_id=reference_id, is_delete=False,  created_by=request.user)
    #     except Course.DoesNotExist:
    #         return None

    #direct use this, exception.py auto detect exception
    def _get_course(self, reference_id):
        return Course.objects.get(reference_id=reference_id,is_deleted=False)

    def get(self, request, reference_id):
        # course = get_object_or_404(Course, reference_id=reference_id, is_deleted=False) #we can also use this
        course = self._get_course(reference_id)

        # data = _course_payload(course)
        return self.success_handler(
            message="Course retrieved successfully.",
            status_code=status.HTTP_200_OK,
            data=_course_payload(course)
        )


    @swagger_auto_schema(
        request_body=CourseSerializer
    )
    def patch(self, request, reference_id):
        # course = get_object_or_404(Course, reference_id=reference_id, is_deleted=False) #we can also use this
        course = self._get_course(reference_id)
        serializer = CourseSerializer(course, data=request.data, partial=True, context={"request": request})
        validate_serializer(serializer)

        user = request.user if request.user.is_authenticated else None

        course = update_instance(course, serializer.validated_data,user)

        # data = _course_payload(course)
        return self.success_handler(
            message="Course updated successfully.",
            status_code=status.HTTP_200_OK, 
            data=_course_payload(course)
        )

    def delete(self, request, reference_id):
        # course = get_object_or_404(Course, reference_id=reference_id, is_deleted=False) #we can also use this
        course = self._get_course(reference_id)
        user = request.user if request.user.is_authenticated else None

        course = delete_instance(course, user)

        # data = _course_payload(course)
        return self.success_handler(
            message="Course deleted successfully.",
            status_code=status.HTTP_200_OK, 
            data=_course_payload(course)
        )








