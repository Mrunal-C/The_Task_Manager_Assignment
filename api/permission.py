from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow admins to edit or delete objects.
    """
    def has_permission(self, request, view):
        # Admins can edit or delete objects, others can only read
        if request.user and request.user.is_staff:
            return True
        return request.method in permissions.SAFE_METHODS
