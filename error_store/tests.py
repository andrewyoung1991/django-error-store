"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.handlers.wsgi import WSGIRequest

from error_store.models import ServerError
from error_store.views import test


class TestServerError(TestCase):
    def setUp(self):
        with self.assertRaises(ServerError.DoesNotExist):
            ServerError.objects.get(id=1)
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 500)

    def test_500_error_creates_server_error_object(self):
        self.assertTrue(ServerError.objects.get(id=1))

    def test_server_error_object_is_request(self):
        request = ServerError.objects.get(id=1)
        self.assert_(isinstance(request.request, WSGIRequest))

    def test_server_error_can_be_passed_to_view_func(self):
        request = ServerError.objects.get(id=1)
        resp = test(request)
        self.assertEqual(resp.status_code, 500)
        self.assertEqual(resp.content, "test error")
