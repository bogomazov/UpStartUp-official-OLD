__author__ = 'andrey'

from rest_framework import permissions

class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user:
            return obj == request.user
        return False
