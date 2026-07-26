from django.urls import path

from apps.authx.api.views import (
    LoginApiView,
    LogoutApiView,
    AdminListCreateApiView,
    AdminDetailApiView
)

urlpatterns = [
    path("login/", LoginApiView.as_view(), name="login"),
    path("logout/", LogoutApiView.as_view(), name="logout"),
    path("admin/", AdminListCreateApiView.as_view(), name="admin-list-create"),
    path("admin/<uuid:reference_id>/", AdminDetailApiView.as_view(), name="admin-detail"),
    
]
