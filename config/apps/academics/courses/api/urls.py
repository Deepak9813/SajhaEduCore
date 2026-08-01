from django.urls import path

from apps.academics.courses.api.views import (
    CourseListCreateAPIView,
    CourseDetailAPIView,
    CourseSearchAPIView,
)


urlpatterns = [
    path("", CourseListCreateAPIView.as_view(), name="course-list-create"),
    path("search/", CourseSearchAPIView.as_view(), name="course-search"),
    path("<uuid:reference_id>/", CourseDetailAPIView.as_view(), name="course-detail"),
]

