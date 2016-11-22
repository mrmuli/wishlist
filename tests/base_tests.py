from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from faker import Factory

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from factories import BucketlistFactory, BucketlistItemFactory, UserFactory

class BaseTest(APITestCase):

    def setUp(self):
        self.fake = Factory.create()
        self.client = APIClient()

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
        self.test_user1 = UserFactory()
        # self.test_user = UserFactory()


        self.single_bucketlist_url = '/api/v1/bucketlists/1'
        self.all_bucketlists__url = '/api/v1/bucketlists/'
        self.create_bucketlist_item__url = '/api/v1/bucketlists/2/items/'
        self.single_bucketlist_item__url = '/api/v1/bucketlists/1/items/1/'

    def login_user1(self):
        "This method logs in user 1 and returns the token"
        # self.create_users(self.test_user1)
        login_url = reverse('login')
        response = self.client.post(login_url, self.test_user1)
        self.token = response.data.get('token')
        return self.token


    def create_users(self, user):
        response = self.client.post(path='/users/', data=user, format='json')
        return response
