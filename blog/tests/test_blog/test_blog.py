import pytest

from django.urls import reverse
from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('keanu', 'reeves@neo.com', 'johnpassword')
#     assert User.objects.count() == 1
#
#
# @pytest.mark.django_db
# def test_home_view(client):
#     url = reverse('home')
#     response = client.get(url)
#     assert response.status_code == 200