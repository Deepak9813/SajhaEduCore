from django.urls import path

from apps.authx.api.views import (
    LoginAPIView,
    LogoutAPIView,
    AdminListCreateAPIView,
    AdminDetailAPIView
)


urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("admin/", AdminListCreateAPIView.as_view(), name="admin-list-create"),
    path("admin/<uuid:reference_id>/", AdminDetailAPIView.as_view(), name="admin-detail"),
    
]
