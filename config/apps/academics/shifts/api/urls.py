from django.urls import path

from apps.academics.shifts.api.views import (
    ShiftListCreateAPIView,
    ShiftDetailAPIView,
    ShiftSearchAPIView,
)


urlpatterns = [
    path("", ShiftListCreateAPIView.as_view(), name="shift-list-create"),
    path("search/", ShiftSearchAPIView.as_view(), name="shift-search"),
    path("<uuid:reference_id>/", ShiftDetailAPIView.as_view(), name="shift-detail"),
]
