# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class KeywordSearchKeywords(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, keywords: List[str]=None):  # noqa: E501
        """KeywordSearchKeywords - a model defined in Swagger

        :param keywords: The keywords of this KeywordSearchKeywords.  # noqa: E501
        :type keywords: List[str]
        """
        self.swagger_types = {
            'keywords': List[str]
        }

        self.attribute_map = {
            'keywords': 'keywords'
        }
        self._keywords = keywords

    @classmethod
    def from_dict(cls, dikt) -> 'KeywordSearchKeywords':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The keyword_search_keywords of this KeywordSearchKeywords.  # noqa: E501
        :rtype: KeywordSearchKeywords
        """
        return util.deserialize_model(dikt, cls)

    @property
    def keywords(self) -> List[str]:
        """Gets the keywords of this KeywordSearchKeywords.


        :return: The keywords of this KeywordSearchKeywords.
        :rtype: List[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords: List[str]):
        """Sets the keywords of this KeywordSearchKeywords.


        :param keywords: The keywords of this KeywordSearchKeywords.
        :type keywords: List[str]
        """
        if keywords is None:
            raise ValueError("Invalid value for `keywords`, must not be `None`")  # noqa: E501

        self._keywords = keywords