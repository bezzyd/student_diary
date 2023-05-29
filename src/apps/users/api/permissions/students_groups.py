from src.apps.users.models.student_groups import StudentGroup
from src.apps.users.models.users import User
from src.apps.users.api.permissions.users import IsTeacher


class IsClassroomTeacher(IsTeacher):
    def has_object_permission(self, request, view, obj: StudentGroup):
        user: User = request.user
        return obj.classrom_teacher == user.teacher_profile
