from rest_framework import serializers

from src.apps.diaries.models.diaries import Diary


class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = "__all__"
