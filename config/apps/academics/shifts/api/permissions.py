
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Allow read access to everyone.
    Allow write access only to admins.
    """

    message = "You do not have permission to modify shifts."

    def has_permission(self, request, view):

        # Public read access
        if request.method in SAFE_METHODS:  # if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Only admin can create/update/delete courses
        user = request.user

        return (
            user.is_authenticated
            and user.is_staff
            and user.role == "admin"
        )
