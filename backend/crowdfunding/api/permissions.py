from rest_framework import permissions


class IsOwnerProjectOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" or request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or request.user.is_superuser:
            return True
        return obj.owner == request.user



class IsSameUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_superuser and ("is_superuser" in request.data or "is_active" in request.data):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "GET" or obj == request.user or request.user.is_superuser:
            return True
        return False




class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET" or request.user.is_superuser:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        return True



class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # get or post in public link
        if request.method == "GET" or request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        # get or put or patch in private link
        if request.method == "GET" or obj.user_id == request.user or request.user.is_superuser:
            return True
        return False




#for reports
class IsAdminOrpost(permissions.BasePermission):
    def has_permission(self, request, view):
        # get or post in public link
        if request.user.is_superuser or (request.method == "POST" and request.user.is_authenticated):
            return True
        return False

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # get or post in public link
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        # get or put or patch in private link
        if obj.user_id == request.user or request.user.is_superuser:
            return True
        return False



class donation(permissions.BasePermission):
    def has_permission(self, request, view):
        # get or post in public link
        if request.user.is_authenticated:
            return True
        return False
    def has_object_permission(self, request, view, obj):
        # get or put or patch in private link
        if request.method == "GET" or request.user.is_superuser:
            return True
        return False


class photoPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        # get or post in public link
        if request.user.is_superuser or request.method == "DELETE":
            return True
        return False
    def has_object_permission(self, request, view, obj):
        # get or put or patch in private link
        if request.user.is_superuser or (request.method == "DELETE" and obj.project.owner == request.user):
            return True
        return False
