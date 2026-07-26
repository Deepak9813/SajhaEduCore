from django.urls import path

from apps.academics.courses.api.views import (
    CourseListCreateApiView,
    CourseDetailApiView,
)


urlpatterns = [
    path("", CourseListCreateApiView.as_view(), name="course-list-create"),
    path("<uuid:reference_id>/", CourseDetailApiView.as_view(), name="course-detail"),
]

