from rest_framework import serializers

from src.apps.users.models.profiles import TeacherProfile


class TeacherSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        source="user.first_name", read_only=True
    )
    last_name = serializers.CharField(
        source="user.last_name", read_only=True
    )

    class Meta:
        model = TeacherProfile
        fields = ("id", "first_name", "last_name", "experience", "education")
