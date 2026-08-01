from django.urls import path

from apps.academics.employees.api.views import (
    EmployeeListCreateAPIView,
    EmployeeDetailAPIView,
    EmployeeSearchAPIView,
)


urlpatterns = [
    path("", EmployeeListCreateAPIView.as_view(), name="employee-list-create"),
    path("search/", EmployeeSearchAPIView.as_view(), name="employee-search"),
    path("<uuid:reference_id>/", EmployeeDetailAPIView.as_view(), name="employee-detail"),
]
