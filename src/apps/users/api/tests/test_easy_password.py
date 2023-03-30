import pytest
from django.urls import reverse
from src.apps.users.const import ProfileChoices


@pytest.mark.django_db
def test_create_user(api_client):
    client = api_client()
    data = {
        'username': 'sanya',
        'first_name': 'Alex',
        'last_name': 'Abraka',
        'profile_type': ProfileChoices.STUDENT,
        'email': 'sanya11@gmail.com',
        'password': '123456',
        'repeated_password': '123456'
    }
    response = client.post(reverse('user-list'), data=data, format='json')
    assert response.status_code == 400, response.data
