from rest_framework.permissions import *
from .models import *



class ReadOnly(BasePermission):
    def has_permission(self, request, view):
         return request.method in SAFE_METHODS


class IsAuthenticate(BasePermission):
       def has_object_permission(self, request, view, obj):

           if request.method in permissions.SAFE_METHODS:
                     return True


           return obj.owner == request.user