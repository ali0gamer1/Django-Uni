from rest_framework import permissions

from daneshgah.models import Professor, Student, IT, DeputyofEducation


class IsProfessorPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, Professor):
            return True
        return False


class IsITPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, IT):
            return True
        return False


class IsDeputyOfEducationPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, DeputyofEducation):
            return True
        return False
