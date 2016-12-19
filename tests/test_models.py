from base_tests import BaseTest
from django.contrib.auth.models import User
from rest_framework import status

class TestUsers(BaseTest):

    def test_user_model_instance(self):
        """ test for model instance """
        u = self.user_creation()
        self.assertTrue(isinstance(u, User))

    def test_successful_user_creation(self):
        """ test for successful user registration """
        response = self.create_users(self.test_user3)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_registration_without_username(self):
        """ test for registration without username """
        user = {'password': self.fake.password()}
        response = self.create_users(user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_registration_without_password(self):
        """ test for registration without password """
        user = {'username': self.fake.user_name()}
        response = self.create_users(user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        """ test for successful user login """
        self.create_users(self.test_user2)
        response = self.client.post('/auth/login/', self.test_user2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_without_password(self):
        """ test for login without password """
        user = {'username': self.fake.user_name()}
        response = self.client.post('/auth/login/', user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_without_username(self):
        """ test for login without username """
        user = {'password': self.fake.password()}
        response = self.client.post('/auth/login/', user)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
