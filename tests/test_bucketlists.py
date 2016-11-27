from base_tests import BaseTest
from rest_framework import status

class TestBucketlists(BaseTest):
    """ Class for all bucketlist endpoints """

    def test_bucketlist_creation(self):
        """Test creation of bucketlists"""
        blist_name = self.fake.first_name()
        data = {'name': blist_name, 'created_by': self.test_user1.id}

        self.get_token()
        url = self.all_bucketlists__url
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bucketlist_creation_without_name(self):
        """ test creation of a bucketlist without a name """
        data = {self.test_user1.id}

        self.get_token()
        url = self.all_bucketlists__url
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_url_on_creation_of_bucketlist(self):
        """ test an invalid url on creating a bucketlist """
        blist_name = self.fake.first_name()
        data = {'name': blist_name, 'created_by': self.test_user1.id}

        self.get_token()
        url = self.all_bucketlists__url + 'be'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_editing_a_bucketlist(self):
        """Test editing a bucketlist"""
        blist_name = 'kamatia'
        data = {'name': blist_name}

        self.get_token()
        url = self.single_bucketlist_url + '1/'
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getting_all_bucketlists(self):
        """Test retrieving all bucketlists """

        self.get_token()
        response = self.client.get(self.all_bucketlists__url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = self.single_bucketlist_url + '1/'
        single_response = self.client.get(url, data)
        self.assertEqual(single_response.status_code, status.HTTP_200_OK)

    def test_bucketlist_deletion(self):
        """ test deletion of a bucketlist """
        self.get_token()
        url = self.single_bucketlist_url + '1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
