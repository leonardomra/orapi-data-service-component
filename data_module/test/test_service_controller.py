# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from data_module.models.health import Health  # noqa: E501
from data_module.test import BaseTestCase


class TestServiceController(BaseTestCase):
    """ServiceController integration test stubs"""

    def test_data_health_get(self):
        """Test case for data_health_get

        
        """
        response = self.client.open(
            '/OR-API/data-api/1.0.0/data/health',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
