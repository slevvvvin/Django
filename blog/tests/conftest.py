import logging
import sys
import uuid

from django.contrib.auth.models import User

import pytest


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def test_password():
    return 'test_pass'


@pytest.fixture
def test_username():
    return 'test_user'


@pytest.fixture
def create_user(test_username, test_password):
    def make_user(**kwargs):
        kwargs['username'] = test_username
        kwargs['password'] = test_password
        return User.objects.create_user(**kwargs)
    return make_user
