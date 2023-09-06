from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = "You must be the admin of this website"

class IsUser(BasePermission):
    message = "You can't modify this user's information"
    def has_permission(self, request, view):
        return bool(request.user.id == view.kwargs.get('pk'))