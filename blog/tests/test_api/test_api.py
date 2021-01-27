import pytest

from django.urls import reverse


class TestAPI:

    @staticmethod
    @pytest.mark.django_db
    def test_user_can_post_token(client, create_user):
        """test possibility for user to create token """

        test_user = create_user()
        data = {
            'username': test_user.username,
            'password': 'test_pass'
        }
        url = reverse('token')
        response = client.post(url, data)
        assert response.status_code == 200
