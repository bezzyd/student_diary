from rest_framework import serializers

from src.apps.users.models.student_groups import StudentGroup


class CurrentTeacherDefault(serializers.CurrentUserDefault):
    def __call__(self, serializer_field):
        return super().__call__(serializer_field).teacher_profile


class StudentGroupSerializer(serializers.ModelSerializer):
    classrom_teacher = serializers.HiddenField(default=CurrentTeacherDefault())

    class Meta:
        model = StudentGroup
        fields = ("year", "classrom_teacher")


class StudentGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentGroup
        fields = ("year", "classrom_teacher", "students")


class AddStudentSerializer(serializers.ModelSerializer):
    ...
