# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.search_result_inner import SearchResultInner  # noqa: F401,E501
from swagger_server import util


class SearchResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self):  # noqa: E501
        """SearchResult - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'SearchResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The search_result of this SearchResult.  # noqa: E501
        :rtype: SearchResult
        """
        return util.deserialize_model(dikt, cls)
