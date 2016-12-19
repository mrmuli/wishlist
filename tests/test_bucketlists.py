from base_tests import BaseTest
from rest_framework import status

class TestBucketlists(BaseTest):
    """ Class for all bucketlist endpoints """

    def test_bucketlist_creation(self):
        """Test creation of bucketlists"""

        self.get_token()
        url = self.all_bucketlists__url
        response = self.client.post(url, data={"name": "named"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_bucketlist_creation_without_name(self):
        """ test creation of a bucketlist without a name """

        self.get_token()
        url = self.all_bucketlists__url
        response = self.client.post(url, data={}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_url_on_creation_of_bucketlist(self):
        """ test an invalid url on creating a bucketlist """
        blist_name = self.fake.first_name()

        self.get_token()
        url = self.all_bucketlists__url + 'be'
        response = self.client.post(url, data={"name": blist_name})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_editing_a_bucketlist(self):
        """Test editing a bucketlist"""

        self.get_token()
        response = self.client.post('/bucketlists/',{'name': 'Test Bucketlist'}, format='json')
        bucket_id = str(response.data['id'])

        url = self.single_bucketlist_url +  bucket_id + '/'
        response = self.client.put(url, data={"name": "kamatia"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getting_all_bucketlists(self):
        """Test retrieving all bucketlists """

        self.get_token()
        response = self.client.post('/bucketlists/',{'name': 'Test Bucketlist'}, format='json')

        response = self.client.get(self.all_bucketlists__url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = self.single_bucketlist_url + '1/'
        single_response = self.client.get(url)
        self.assertEqual(single_response.status_code, status.HTTP_200_OK)

    def test_bucketlist_deletion(self):
        """ test deletion of a bucketlist """
        self.get_token()
        response = self.client.post('/bucketlists/',{'name': 'Deleting Bucketlist'}, format='json')
        bucket_id = str(response.data['id'])

        url = self.single_bucketlist_url +  bucket_id + '/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
