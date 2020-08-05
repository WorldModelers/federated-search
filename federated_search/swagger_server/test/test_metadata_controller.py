# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.metadata_result import MetadataResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMetadataController(BaseTestCase):
    """MetadataController integration test stubs"""

    def test_metadata_data_location_id_value_get(self):
        """Test case for metadata_data_location_id_value_get

        Obtain variabile/dataset metadata
        """
        response = self.client.open(
            '/metadata/{data_location}/{id_value}'.format(data_location='data_location_example', id_value='id_value_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
