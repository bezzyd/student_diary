from django.urls import path

from src.apps.diaries.api.views.diaries import StudentOwnerDiary


urlpatterns = [
    path("<str:username>", StudentOwnerDiary.as_view(), name="diary-detail"),
    ]
