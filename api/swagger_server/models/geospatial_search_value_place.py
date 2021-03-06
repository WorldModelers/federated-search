# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GeospatialSearchValuePlace(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, area_name: List[str]=None):  # noqa: E501
        """GeospatialSearchValuePlace - a model defined in Swagger

        :param area_name: The area_name of this GeospatialSearchValuePlace.  # noqa: E501
        :type area_name: List[str]
        """
        self.swagger_types = {
            'area_name': List[str]
        }

        self.attribute_map = {
            'area_name': 'area_name'
        }
        self._area_name = area_name

    @classmethod
    def from_dict(cls, dikt) -> 'GeospatialSearchValuePlace':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The geospatial_search_value_place of this GeospatialSearchValuePlace.  # noqa: E501
        :rtype: GeospatialSearchValuePlace
        """
        return util.deserialize_model(dikt, cls)

    @property
    def area_name(self) -> List[str]:
        """Gets the area_name of this GeospatialSearchValuePlace.


        :return: The area_name of this GeospatialSearchValuePlace.
        :rtype: List[str]
        """
        return self._area_name

    @area_name.setter
    def area_name(self, area_name: List[str]):
        """Sets the area_name of this GeospatialSearchValuePlace.


        :param area_name: The area_name of this GeospatialSearchValuePlace.
        :type area_name: List[str]
        """
        if area_name is None:
            raise ValueError("Invalid value for `area_name`, must not be `None`")  # noqa: E501

        self._area_name = area_name
