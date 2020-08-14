# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.metadata_result_meta import MetadataResultMeta  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMetadataController(BaseTestCase):
    """MetadataController integration test stubs"""

    def test_metadata_data_location_dataset_id_get(self):
        """Test case for metadata_data_location_dataset_id_get

        Obtain metadata for ISI/NYU datasets
        """
        query_string = [('variable_id', 'variable_id_example')]
        response = self.client.open(
            '/metadata/{data_location}/{dataset_id}'.format(data_location='data_location_example', dataset_id='dataset_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
