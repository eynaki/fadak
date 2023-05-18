from rest_framework.permissions import BasePermission


class IsOwnerOrReadeOnly(BasePermission):
    message = 'permission denied, you are not the owner '

    def has_object_permission(self, request, view, obj):
        if request.method == "PUT" or "PATCH":
            return request.user.is_staff or obj.user_name == request.user
