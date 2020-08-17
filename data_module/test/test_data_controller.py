# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from data_module.models.dataset import Dataset  # noqa: E501
from data_module.test import BaseTestCase


class TestDataController(BaseTestCase):
    """DataController integration test stubs"""

    def test_data_kind_get(self):
        """Test case for data_kind_get

        
        """
        query_string = [('limit', 100)]
        response = self.client.open(
            '/OR-API/data-api/1.0.0/data/{kind}'.format(kind='kind_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_kind_id_delete(self):
        """Test case for data_kind_id_delete

        
        """
        response = self.client.open(
            '/OR-API/data-api/1.0.0/data/{kind}/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d', kind='kind_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_kind_id_get(self):
        """Test case for data_kind_id_get

        
        """
        response = self.client.open(
            '/OR-API/data-api/1.0.0/data/{kind}/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d', kind='kind_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_kind_id_put(self):
        """Test case for data_kind_id_put

        
        """
        headers = [('label', 'label_example')]
        response = self.client.open(
            '/OR-API/data-api/1.0.0/data/{kind}/{id}'.format(id='38400000-8cf0-11bd-b23e-10b96e4ef00d', kind='kind_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_kind_upload_post(self):
        """Test case for data_kind_upload_post

        
        """
        data = dict(file_name='file_name_example',
                    label='label_example')
        response = self.client.open(
            '/OR-API/data-api/1.0.0/data/{kind}/upload'.format(kind='kind_example'),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
