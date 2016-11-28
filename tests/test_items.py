from base_tests import BaseTest
from rest_framework import status

class TestItems(BaseTest):

    def test_item_creation(self):
        """Test creation of bucketlist items"""

        self.get_token()
        response = self.client.post('/bucketlists/',{'name': 'Test Bucketlist'}, format='json')
        bucket_id = str(response.data['id'])
        url = '/bucketlists/' + bucket_id + '/items/'
        response = self.client.post(url, data={"item_name": "named"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_editing_an_item(self):
        """Test editing an item"""

        self.get_token()

        response = self.client.post('/bucketlists/',{'name': 'Test Bucketlist'}, format='json')
        bucket_id = str(response.data['id'])
        url = '/bucketlists/' + bucket_id + '/items/'

        response = self.client.post(url, data={"item_name": "named"}, format='json')
        item_id = str(response.data['id'])

        url = '/bucketlists/' + bucket_id + '/items/' + item_id + '/'
        response = self.client.put(url, data={'item_name': "apple"}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_editing_an_item_that_does_not_exist(self):
        """Test editing a none-existent item"""
        name = 'apple'
        data = {'name': name}

        self.get_token()
        url = self.single_bucketlist_item__url + '465/'
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_item_deletion(self):
        """ test deletion of an item """
        self.get_token()

        response = self.client.post('/bucketlists/',{'name': 'Test Bucketlist'}, format='json')
        bucket_id = str(response.data['id'])
        url = '/bucketlists/' + bucket_id + '/items/'

        response = self.client.post(url, data={"item_name": "named"}, format='json')
        item_id = str(response.data['id'])

        url = '/bucketlists/' + bucket_id + '/items/' + item_id + '/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_deleting_an_item_that_does_not_exist(self):
        """Test deletion of a none-existent item"""
        name = 'mac'
        data = {'name': name}

        self.get_token()
        url = self.single_bucketlist_item__url + '465/'
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
