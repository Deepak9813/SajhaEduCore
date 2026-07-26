from rest_framework.permissions import BasePermission


class IsSuperUser(BasePermission):
    """
    Allow only Django superusers.
    """

    message = "Superuser permission required."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )


class IsAdminUser(BasePermission):   #IsPlatformUser
    """
    Allow only institute admins.

    In SajhaEduCore:
    Django is_staff represents admin access.
    """

    message = "Admin permission required."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_staff       #i.e. request.user.role == "admin"
            and request.user.role == "admin"
        )


class BaseRolePermission(BasePermission):
    """
    Base permission for application roles.
    """

    allowed_roles = ()
    message = "Role permission required."

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in self.allowed_roles
        )


class IsTeacherUser(BaseRolePermission):
    """
    Allow teachers only.
    """

    allowed_roles = ("teacher",)
    message = "Teacher permission required."


class IsEmployeeUser(BaseRolePermission):
    """
    Allow employees only.
    """

    allowed_roles = ("employee",)
    message = "Employee permission required."


class IsStudentUser(BaseRolePermission):
    """
    Allow students only.
    """

    allowed_roles = ("student",)
    message = "Student permission required."
