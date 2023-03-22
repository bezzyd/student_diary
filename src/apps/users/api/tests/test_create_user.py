import pytest
from rest_framework.test import APIClient
from django.urls import reverse


@pytest.mark.django_db
def test_create_user():
    client = APIClient
    data = {
        'username': 'sanya',
        'email': 'sanya11@gmail.com',
        'password': '123fdsfdsaQ~'
    }
    response = client.post(reverse('user-create'), data=data, format='json')
    assert response.status_code == 201, response.data
