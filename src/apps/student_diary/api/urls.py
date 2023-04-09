from django.urls import path

from src.apps.student_diary.api.views import StudentOwnerDiary


urlpatterns = [
    path("<str:username>", StudentOwnerDiary.as_view(), name="diary-detail")
]
