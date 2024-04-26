from rest_framework.permissions import BasePermission


class LeaveBasicPermission(BasePermission):
    message = "Access Permission Denied"

    def has_permission(self, request, view):
        return request.user.has_perms((
                                       'attendances.add_attendance',
                                       'attendances.view_attendance'))
