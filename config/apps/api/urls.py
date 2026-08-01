#apps/api/urls.py: central API URL/router
from django.urls import path, include


urlpatterns = [
    path("auth/", include("apps.authx.api.urls")),
    path("courses/", include("apps.academics.courses.api.urls")),
    path("shifts/", include("apps.academics.shifts.api.urls")),
    path("employees/", include("apps.academics.employees.api.urls")),

]
