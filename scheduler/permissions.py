from rest_framework import permissions

from django.contrib.auth.models import User
from account.models import Client, Employee, Psychologist

class IsClientTherapyOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
         return obj.client_id == Client.objects.get(user=User.objects.get(id=request.user.id)).id

class IsEmployeeProfileOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id

class IsPsychologistTherapyOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, obj):
        return obj.psychologists_id == Psychologist.objects.get(employee=Employee.objects.get(user=User.objects.get(id=request.user.id))).id

