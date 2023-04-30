from rest_framework import serializers

from src.apps.diaries.models.student_diary import StudentDiary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDiary
        fields = "__all__"
