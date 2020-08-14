# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDownloadController(BaseTestCase):
    """DownloadController integration test stubs"""

    def test_download_data_location_dataset_id_get(self):
        """Test case for download_data_location_dataset_id_get

        Download NYU datasets
        """
        response = self.client.open(
            '/download/{data_location}/{dataset_id}'.format(data_location='data_location_example', dataset_id='dataset_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_download_variables_data_location_dataset_id_post(self):
        """Test case for download_variables_data_location_dataset_id_post

        Download ISI variables
        """
        body = ['[ \"access_to_electricity_of_population\", \"access_to_clean_fuels_and_technologies_for_cooking_of_population\" ]']
        response = self.client.open(
            '/download_variables/{data_location}/{dataset_id}'.format(data_location='data_location_example', dataset_id='dataset_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
