from rest_framework.permissions import IsAdminUser


class IsAdmin(IsAdminUser):

    def has_permission(self, request, view):
        return request.user.is_staff
