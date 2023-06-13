from rest_framework import serializers

from src.apps.users.models.student_groups import StudentGroup


class CurrentTeacherDefault(serializers.CurrentUserDefault):
    def __call__(self, serializer_field):
        return super().__call__(serializer_field).teacher_profile


class StudentGroupSerializer(serializers.HyperlinkedModelSerializer):
    classroom_teacher = serializers.HiddenField(
        default=CurrentTeacherDefault()
        )

    class Meta:
        model = StudentGroup
        fields = ("year", "classroom_teacher")


class AddStudentSerializer(serializers.ModelSerializer):
    pass
