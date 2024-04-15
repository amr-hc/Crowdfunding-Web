from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return obj.owner == request.user

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return False


class IsSameUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        elif "is_superuser" in request.data or "is_active" in request.data:
            return False
        return obj == request.user

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        elif "is_superuser" in request.data or "is_active" in request.data:
            return False
        return True


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return False

class IsOwnerCommentOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # get or post in public link
        if request.method == "GET" or request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        # get or put or patch in private link
        if request.method == "GET" or (request.method == "PATCH" and obj.user_id.id == request.user.id) or request.user.is_superuser:
            return True
        return False






