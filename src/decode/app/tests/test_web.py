from unittest import mock

from django.test import TestCase
from django.urls import reverse


class TestWeb(TestCase):
    def test_decode_get(self):
        """
        Ensure end-user decode page is created as expected.
        """
        response = self.client.get(reverse("web-decode"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Decoder", html=True)

    @mock.patch("app.web._process")
    def test_decode_post(self, mock_process):
        """
        Ensure proper result is included in page when submitted by end-user.
        """
        mock_process.return_value = ["BBB", "BZ", "VF"]
        response = self.client.post(reverse("web-decode"), {"input_str": "226"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BBB", html=True)
        self.assertContains(response, "BZ", html=True)
        self.assertContains(response, "VF", html=True)
