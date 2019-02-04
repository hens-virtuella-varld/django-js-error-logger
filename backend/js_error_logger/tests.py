from django.test import TestCase
from django.urls import reverse
from .models import JSError


class CreateViewTests(TestCase):
    def test_with_valid_data(self):
        valid_data = {
            'name': 'JSErrorName',
            'app_id': 'test-app',
            'user': 'test-user',
            'time': '2019-02-04 10:32:33',
            'url': 'test.com',
            'status': 'some-status',
            'message': 'some-message',
            'stack': 'some-stack'
        }
        response = self.client.post(reverse('js_error_logger:create'), valid_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(JSError.objects.all().count(), 1)
    def test_with_invalid_data(self):
        invalid_data = {}
        response = self.client.post(reverse('js_error_logger:create'), invalid_data)
        self.assertEqual(response.status_code, 400)
