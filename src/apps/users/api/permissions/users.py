from rest_framework.permissions import (
    BasePermission, SAFE_METHODS,
    IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
)


class IsAdminOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or super().has_permission(request, view)
        )


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user.student_profile)


class IsTeacher(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(
            request, view) and request.user.is_teacher


class IsTeacherOrReadOnly(IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        return super().has_permission(
            request, view) and request.user.is_teacher
