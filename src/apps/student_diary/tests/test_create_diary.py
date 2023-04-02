import pytest
from rest_framework.reverse import reverse

from src.apps.users.const import ProfileChoices
from src.apps.users.models.users import User


@pytest.mark.django_db
def test_get_diary_by_username(api_client):
    client = api_client()
    user = User.objects.create_user(
        email="ruslan@korneev.ru",
        password="123",
        username="ruslan",
        profile_type=ProfileChoices.STUDENT
    )
    client.force_authenticate(user)
    
    response = client.get(reverse("diary-detail", kwargs={"username": user.username}))
    assert response.status_code == 200, response.data


    user2 = User.objects.create_user(
        email="sanya@bez.ru",
        password="123",
        username="sanya",
        profile_type=ProfileChoices.STUDENT
    )

    client.force_authenticate(user2)
    response = client.get(reverse("diary-detail", kwargs={"username": user.username}))
    assert response.status_code == 403, user2.student_profile.student_diary.filter(
            pk=user.student_profile.student_diary.first().pk).exists()
