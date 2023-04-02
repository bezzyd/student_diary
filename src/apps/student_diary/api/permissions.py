from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        result = request.user.student_profile.student_diary.filter(pk=obj.pk).exists()
        print(result)
        return result
