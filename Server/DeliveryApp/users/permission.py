from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None

def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsSuperUser(permissions.BasePermission):
    required_groups = ['Superuser']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class IsStaff(permissions.BasePermission):
    required_groups = ['Staff']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class IsDeliveryman(permissions.BasePermission):
    required_groups = ['Deliveryman']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission


class IsRestaurantAdmin(permissions.BasePermission):
    required_groups = ['Restaurant admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission



class IsClient(permissions.BasePermission):
    required_groups = ['Client']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

