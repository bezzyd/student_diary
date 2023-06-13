from rest_framework import serializers

from src.apps.users.models.profiles import StudentProfile


class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(
        source="user.first_name", read_only=True
    )
    last_name = serializers.CharField(
        source="user.last_name", read_only=True
    )

    class Meta:
        model = StudentProfile
        fields = ("id", "first_name", "last_name", "group")
