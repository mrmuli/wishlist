from base_tests import BaseTest
from rest_framework import status
from api.models import Bucketlist

class TestBucketlists(BaseTest):
    """ Class for all bucketlist endpoints """

    def test_bucketlist_creation(self):
        """Test creation of bucketlists"""
        blist_name = self.fake.first_name()
        data = {'name': blist_name}

        self.login_user1()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = self.client.post(self.all_bucketlists__url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_editing_a_bucketlist(self):
        """Test editing a bucketlist"""
        blist_name = 'kamatia'
        data = {'name': blist_name}

        self.login_user1()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

        response = self.client.put(self.single_bucketlist_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getting_all_bucketlists(self):
        """Test retrieving all bucketlists """

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get(self.all_bucketlists__url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        single_response = self.client.get(self.single_bucketlist_url, data)
        self.assertEqual(single_response.status_code, status.HTTP_200_OK)
