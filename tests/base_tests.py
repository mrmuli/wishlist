from django.test import TestCase
from faker import Faker, Factory

from rest_framework.test import APITestCase
from rest_framework import status


class BaseTest(APITestCase):

    def setUp(self):
        self.fake = Factory.create()

        self.test_user1 = {
        'username': self.fake.user_name(),
        'first_name': self.fake.first_name(),
        'last_name': self.fake.last_name(),
        'password': self.fake.password(),
        'email': self.fake.email()
        }
        self.test_user2 = {
        'username': self.fake.user_name(),
        'first_name': self.fake.first_name(),
        'last_name': self.fake.last_name(),
        'password': self.fake.password(),
        'email': self.fake.email()
        }

    def create_users(self, user):
        response = self.client.post(path='/users/',
        data=user,
        format='json')
        return response
