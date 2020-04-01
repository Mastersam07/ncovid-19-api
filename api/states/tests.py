from django.test import TestCase
from rest_framework.test import APIRequestFactory, APITestCase

from states import apiviews


class TestState(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.StateViewSet.as_view({'get': 'list'})
        self.uri = '/api/states/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
