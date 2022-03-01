from rest_framework import permissions

from django.contrib.auth.models import User
from account.models import Client, Employee, Psychologist

class IsClientTherapyOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and Client.objects.get(user=request.user)

    # for object level permissions
    def has_object_permission(self, request, view, obj):
         return obj.client == Client.objects.get(user=request.user)

class IsEmployeeProfileOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and Employee.objects.get(user=request.user)

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.employee == Employee.objects.get(user=request.user)

class IsPsychologistTherapyOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and Psychologist.objects.get(employee=Employee.objects.get(user=request.user))

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.psychologist == Psychologist.objects.get(employee=Employee.objects.get(user=request.user))

