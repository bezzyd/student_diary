from rest_framework import serializers

from src.apps.student_diary.models.student_diary import StudentDiary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDiary
        fields = "__all__"
