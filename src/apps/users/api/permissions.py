from rest_framework.permissions import (
    BasePermission, SAFE_METHODS,
    IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
)

from src.apps.users.models.student_groups import StudentGroup
from src.apps.users.models.users import User


class IsAdminOrReadOnly(IsAdminUser):  # users
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS
            or super().has_permission(request, view)
        )


class IsStudent(BasePermission):  # users
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user.student_profile)


class IsTeacher(IsAuthenticated):  # users
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_teacher


class IsTeacherOrReadOnly(IsAuthenticatedOrReadOnly):  # users
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_teacher


class IsClassroomTeacher(IsTeacher):  # students_groups
    def has_object_permission(self, request, view, obj: StudentGroup):
        user: User = request.user
        return obj.classrom_teacher == user.teacher_profile
