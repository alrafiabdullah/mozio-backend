import json
import pdb

from django import urls
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Provider, ServiceArea
from .serializers import ProviderSerializer

# Create your tests here.


class TestSetUp(APITestCase):
    def setUp(self):
        self.provider_url = reverse('provider')
        self.service_url = reverse('service_area')

        self.provider_data = {
            "name": "Test Provider",
            "email": "test@test.com",
            "phone_number": "+8801913659072",
            "language": "en",
            "currency": "usd",
        }

        self.update_provider_data = {
            "id": 1,
            "name": "Test Provider Updated",
        }

        self.id_provider_data = {
            "id": 1
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestViews(TestSetUp):
    """
        Provider API Tests
    """

    def test_creating_provider_properly(self):
        response = self.client.post(
            self.provider_url, self.provider_data, format='json')

        # pdb.set_trace()
        self.assertEqual(response.data['name'], self.provider_data['name'])
        self.assertEqual(response.data['email'], self.provider_data['email'])
        self.assertEqual(response.data['language'],
                         self.provider_data['language'])
        self.assertEqual(response.data['currency'],
                         self.provider_data['currency'])
        self.assertEqual(response.status_code, 201)

    def test_creating_provider_with_no_data(self):
        response = self.client.post(self.provider_url)
        self.assertEqual(response.status_code, 400)

    def test_getting_provider_list(self):
        Provider.objects.create(**self.provider_data)
        response = self.client.get(
            self.provider_url, self.update_provider_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_deleting_provider(self):
        Provider.objects.create(**self.provider_data)
        response = self.client.delete(
            self.provider_url, self.id_provider_data, format='json')
        # pdb.set_trace()
        self.assertEqual(response.status_code, 200)

    """
        Service Area API Tests
    """

    def test_creating_service_area_properly(self):
        temp_prod = Provider.objects.create(**self.provider_data)
        ServiceArea.objects.create(
            provider=temp_prod,
            name="Test Service Area",
            price=50.0,
            location="SRID=4326 POLYGON((90.366862 23.808394, 90.371454 23.808355, 90.37151799999999 23.804978, 90.367377 23.804272, 90.364952 23.806569, 90.366862 23.808394))",
        )
        response = self.client.post(
            self.service_url, self.service_data, format='json')

        self.assertEqual(response.data['name'], self.service_data['name'])
        self.assertEqual(response.data['price'], self.service_data['price'])
        self.assertEqual(response.data['location'],
                         self.service_data['location'])
        self.assertEqual(response.data['provider'],
                         self.service_data['provider'])
        self.assertEqual(response.status_code, 201)

    def test_creating_service_area_with_no_data(self):
        response = self.client.post(self.service_url)
        self.assertEqual(response.status_code, 400)

    def test_getting_service_area_list(self):
        temp_prod = Provider.objects.create(**self.provider_data)
        ServiceArea.objects.create(
            provider=temp_prod,
            name="Test Service Area",
            price=50.0,
            location="SRID=4326 POLYGON((90.366862 23.808394, 90.371454 23.808355, 90.37151799999999 23.804978, 90.367377 23.804272, 90.364952 23.806569, 90.366862 23.808394))",
        )

        response = self.client.get(
            self.service_url, self.id_provider_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_deleting_service_area(self):
        temp_prod = Provider.objects.create(**self.provider_data)
        ServiceArea.objects.create(
            provider=temp_prod,
            name="Test Service Area",
            price=50.0,
            location="SRID=4326 POLYGON((90.366862 23.808394, 90.371454 23.808355, 90.37151799999999 23.804978, 90.367377 23.804272, 90.364952 23.806569, 90.366862 23.808394))",
        )
        response = self.client.delete(
            self.service_url, self.id_provider_data, format='json')
        self.assertEqual(response.status_code, 200)
