import pytest
from django.urls import reverse
from src.apps.users.const import ProfileChoices
from src.apps.users.models.users import User


@pytest.mark.django_db
def test_create_user(api_client):
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
    assert User.objects.filter(pk=response.data['pk']).exists()
    user = User.objects.get(pk=response.data['pk'])
    assert user.is_student
    assert not user.is_teacher
