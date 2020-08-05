# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class DataLocation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data_location: str='All'):  # noqa: E501
        """DataLocation - a model defined in Swagger

        :param data_location: The data_location of this DataLocation.  # noqa: E501
        :type data_location: str
        """
        self.swagger_types = {
            'data_location': str
        }

        self.attribute_map = {
            'data_location': 'data_location'
        }
        self._data_location = data_location

    @classmethod
    def from_dict(cls, dikt) -> 'DataLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The data_location of this DataLocation.  # noqa: E501
        :rtype: DataLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data_location(self) -> str:
        """Gets the data_location of this DataLocation.


        :return: The data_location of this DataLocation.
        :rtype: str
        """
        return self._data_location

    @data_location.setter
    def data_location(self, data_location: str):
        """Sets the data_location of this DataLocation.


        :param data_location: The data_location of this DataLocation.
        :type data_location: str
        """
        allowed_values = ["ISI", "NYU", "All"]  # noqa: E501
        if data_location not in allowed_values:
            raise ValueError(
                "Invalid value for `data_location` ({0}), must be one of {1}"
                .format(data_location, allowed_values)
            )

        self._data_location = data_location