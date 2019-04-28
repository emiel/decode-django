from unittest import mock

from django.test import TestCase

from app.api_client import ApiClient


class TestApiClient(TestCase):
    @mock.patch("requests.Session.request")
    def test_decode(self, mock_request):
        """
        Ensure ApiClient decode method makes proper HTTP request
        """
        ApiClient().decode("226")

        mock_request.assert_called_once_with(
            "get", mock.ANY, data=None, params={"input": "226"}
        )
