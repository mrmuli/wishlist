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

        self.test_user3 = {
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
        self.test_user1 = UserFactory(username='muli', password='passsword')
        self.test_user4 = UserFactory(username='mike')


        self.single_bucketlist_url = '/bucketlists/'
        self.all_bucketlists__url = '/bucketlists/'
        self.create_bucketlist_item__url = '/bucketlists/1/items/'
        self.single_bucketlist_item__url = '/bucketlists/1/items/'

    def user_creation(self, username='jojo', first_name='joseph', last_name='muli', email='joseph.muli@andela.com', password='master12'):
        return User.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

    def create_users(self, user):
        response = self.client.post(path='/auth/register/', data=user, format='json')
        return response

    def login_user1(self):
        "This method logs in user 1 and returns the token"
        self.client.post('/auth/register/',{'username': 'test', 'password': 'test', 'email': 'test@mail.com'}, format='json')
        response = self.client.post('/auth/login/',data={'username': 'test', 'password': 'test'}, format='json')
        self.token = response.data['auth_token']
        return self.token

    def get_token(self):
        """ Set Header token """
        self.login_user1()
        self.client.force_authenticate(token=self.token)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
