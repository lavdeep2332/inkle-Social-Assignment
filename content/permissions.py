from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Owner can delete
        if obj.author == request.user:
            return True
        # Admin can delete
        if request.method == 'DELETE' and request.user.role in ['admin', 'owner']:
            return True
        return False