import pytest
from django.urls import reverse
from src.apps.users.const import ProfileChoices
from src.apps.users.models.users import User


@pytest.mark.django_db
@pytest.mark.parametrize(
        'password, repeated_password, status_code', [
            ('123fdsfdsaQ~', '123fdsfdsaQ~', 201),
            ('123456', '123456', 400),
            ('123fdsfdsaQ~', '123fdsfdsaQW', 400),
            ]
        )
def test_create_user(api_client, password, repeated_password, status_code):
    client = api_client()
    data = {
        'username': 'sanya',
        'first_name': 'Alex',
        'last_name': 'Abraka',
        'profile_type': ProfileChoices.STUDENT,
        'email': 'sanya11@gmail.com',
        'password': password,
        'repeated_password': repeated_password
    }
    response = client.post(reverse('user-list'), data=data, format='json')
    assert response.status_code == status_code, response.data


@pytest.mark.django_db
def test_create_student():
    data = {
        'username': 'sanya',
        'first_name': 'Alex',
        'last_name': 'Abraka',
        'profile_type': ProfileChoices.STUDENT,
        'email': 'sanya11@gmail.com',
        'password': '123fdsfdsaQ~',
    }
    user = User.objects.create_user(**data)
    assert user.is_student
    assert not user.is_teacher
    assert hasattr(user.student_profile, 'student_diary')


@pytest.mark.django_db
def test_create_teacher():
    data = {
        'username': 'sanya',
        'first_name': 'Alex',
        'last_name': 'Abraka',
        'profile_type': ProfileChoices.TEACHER,
        'email': 'sanya11@gmail.com',
        'password': '123fdsfdsaQ~',
    }
    user = User.objects.create_user(**data)
    assert user.is_teacher
    assert not user.is_student
