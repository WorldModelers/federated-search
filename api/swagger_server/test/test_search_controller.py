# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.search_result import SearchResult  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSearchController(BaseTestCase):
    """SearchController integration test stubs"""

    def test_search_concepts_concept_name_get(self):
        """Test case for search_concepts_concept_name_get

        Concept based search
        """
        response = self.client.open(
            '/search_concepts/{concept_name}'.format(concept_name='concept_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_post(self):
        """Test case for search_post

        Search over Datamarts
        """
        body = Body()
        response = self.client.open(
            '/search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
