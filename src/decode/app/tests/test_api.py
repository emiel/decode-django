from django.test import TestCase
from django.urls import reverse


class TestApi(TestCase):
    def test_decode_success(self):
        """
        Ensure decode endpoint invokes decode successfully.
        """
        response = self.client.get(reverse("api-decode"), data={"input": "226"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": ["BBF", "BZ", "VF"]})

    def test_decode_input_invalid(self):
        """
        Ensure decode endpoint returns 400 when given invalid input.
        """
        response = self.client.get(reverse("api-decode"), data={"input": "abc"})
        self.assertEqual(response.status_code, 400)
