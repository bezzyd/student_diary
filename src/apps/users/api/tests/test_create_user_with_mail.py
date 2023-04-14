import pytest
from django.urls import reverse
from rest_framework import status
from src.apps.users.const import ProfileChoices
from src.apps.users.models.users import User


@pytest.mark.django_db
@pytest.mark.parametrize(
      'status_code', 'created', [
        (201, True),
        (400, False),
        ]
    )
def test_create_user(api_client, status_code, created, mailoutbox):
    client = api_client()
    data = {
        'username': 'sanya',
        'first_name': 'Alex',
        'last_name': 'Abraka',
        'profile_type': ProfileChoices.STUDENT,
        'email': 'sanya11@gmail.com',
        'password': '123fdsfdsaQ~',
        'repeated_password': '123fdsfdsaQ~'
    }
    response = client.post(reverse('user-list'), data=data, format='json')
    if created:
        user = User.objects.get(pk=response.data['pk'])
        assert not user.is_active
        assert len(mailoutbox) == 1
        message = mailoutbox['code']
        response = client.get(reverse('user-verify', args=(message)))
        if response.status_code == status.HTTP_200_OK:
            user.refresh_from_db()
            assert user.is_active
