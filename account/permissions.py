from rest_framework import permissions


class IsClientProfileOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id and obj.is_verified==True

class IsEmployeeProfileOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id 

class IsPsychologistProfileOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.employee.user.id == request.user.id


class IsSuperAdmin(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_superuser

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser