# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class GeospatialSearchValueBbox(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, latitude1: float=None, longitude1: float=None, latitude2: float=None, longitude2: float=None):  # noqa: E501
        """GeospatialSearchValueBbox - a model defined in Swagger

        :param latitude1: The latitude1 of this GeospatialSearchValueBbox.  # noqa: E501
        :type latitude1: float
        :param longitude1: The longitude1 of this GeospatialSearchValueBbox.  # noqa: E501
        :type longitude1: float
        :param latitude2: The latitude2 of this GeospatialSearchValueBbox.  # noqa: E501
        :type latitude2: float
        :param longitude2: The longitude2 of this GeospatialSearchValueBbox.  # noqa: E501
        :type longitude2: float
        """
        self.swagger_types = {
            'latitude1': float,
            'longitude1': float,
            'latitude2': float,
            'longitude2': float
        }

        self.attribute_map = {
            'latitude1': 'latitude1',
            'longitude1': 'longitude1',
            'latitude2': 'latitude2',
            'longitude2': 'longitude2'
        }
        self._latitude1 = latitude1
        self._longitude1 = longitude1
        self._latitude2 = latitude2
        self._longitude2 = longitude2

    @classmethod
    def from_dict(cls, dikt) -> 'GeospatialSearchValueBbox':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The geospatial_search_value_bbox of this GeospatialSearchValueBbox.  # noqa: E501
        :rtype: GeospatialSearchValueBbox
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latitude1(self) -> float:
        """Gets the latitude1 of this GeospatialSearchValueBbox.

        The latitude of the top left point.  # noqa: E501

        :return: The latitude1 of this GeospatialSearchValueBbox.
        :rtype: float
        """
        return self._latitude1

    @latitude1.setter
    def latitude1(self, latitude1: float):
        """Sets the latitude1 of this GeospatialSearchValueBbox.

        The latitude of the top left point.  # noqa: E501

        :param latitude1: The latitude1 of this GeospatialSearchValueBbox.
        :type latitude1: float
        """
        if latitude1 is None:
            raise ValueError("Invalid value for `latitude1`, must not be `None`")  # noqa: E501

        self._latitude1 = latitude1

    @property
    def longitude1(self) -> float:
        """Gets the longitude1 of this GeospatialSearchValueBbox.

        The longitude of the top left point.  # noqa: E501

        :return: The longitude1 of this GeospatialSearchValueBbox.
        :rtype: float
        """
        return self._longitude1

    @longitude1.setter
    def longitude1(self, longitude1: float):
        """Sets the longitude1 of this GeospatialSearchValueBbox.

        The longitude of the top left point.  # noqa: E501

        :param longitude1: The longitude1 of this GeospatialSearchValueBbox.
        :type longitude1: float
        """
        if longitude1 is None:
            raise ValueError("Invalid value for `longitude1`, must not be `None`")  # noqa: E501

        self._longitude1 = longitude1

    @property
    def latitude2(self) -> float:
        """Gets the latitude2 of this GeospatialSearchValueBbox.

        The latitude of the bottom right point.  # noqa: E501

        :return: The latitude2 of this GeospatialSearchValueBbox.
        :rtype: float
        """
        return self._latitude2

    @latitude2.setter
    def latitude2(self, latitude2: float):
        """Sets the latitude2 of this GeospatialSearchValueBbox.

        The latitude of the bottom right point.  # noqa: E501

        :param latitude2: The latitude2 of this GeospatialSearchValueBbox.
        :type latitude2: float
        """
        if latitude2 is None:
            raise ValueError("Invalid value for `latitude2`, must not be `None`")  # noqa: E501

        self._latitude2 = latitude2

    @property
    def longitude2(self) -> float:
        """Gets the longitude2 of this GeospatialSearchValueBbox.

        The longitude of the bottom right point.  # noqa: E501

        :return: The longitude2 of this GeospatialSearchValueBbox.
        :rtype: float
        """
        return self._longitude2

    @longitude2.setter
    def longitude2(self, longitude2: float):
        """Sets the longitude2 of this GeospatialSearchValueBbox.

        The longitude of the bottom right point.  # noqa: E501

        :param longitude2: The longitude2 of this GeospatialSearchValueBbox.
        :type longitude2: float
        """
        if longitude2 is None:
            raise ValueError("Invalid value for `longitude2`, must not be `None`")  # noqa: E501

        self._longitude2 = longitude2