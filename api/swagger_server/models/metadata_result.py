# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MetadataResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, description: str=None, dataset_id: str=None, variable_id: str=None, url: str=None, source: str=None, spatial_resolution: str=None, temporal_resolution: str=None, z_meta: List[object]=None):  # noqa: E501
        """MetadataResult - a model defined in Swagger

        :param name: The name of this MetadataResult.  # noqa: E501
        :type name: str
        :param description: The description of this MetadataResult.  # noqa: E501
        :type description: str
        :param dataset_id: The dataset_id of this MetadataResult.  # noqa: E501
        :type dataset_id: str
        :param variable_id: The variable_id of this MetadataResult.  # noqa: E501
        :type variable_id: str
        :param url: The url of this MetadataResult.  # noqa: E501
        :type url: str
        :param source: The source of this MetadataResult.  # noqa: E501
        :type source: str
        :param spatial_resolution: The spatial_resolution of this MetadataResult.  # noqa: E501
        :type spatial_resolution: str
        :param temporal_resolution: The temporal_resolution of this MetadataResult.  # noqa: E501
        :type temporal_resolution: str
        :param z_meta: The z_meta of this MetadataResult.  # noqa: E501
        :type z_meta: List[object]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'dataset_id': str,
            'variable_id': str,
            'url': str,
            'source': str,
            'spatial_resolution': str,
            'temporal_resolution': str,
            'z_meta': List[object]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'dataset_id': 'dataset_id',
            'variable_id': 'variable_id',
            'url': 'url',
            'source': 'source',
            'spatial_resolution': 'spatial_resolution',
            'temporal_resolution': 'temporal_resolution',
            'z_meta': 'z_meta'
        }
        self._name = name
        self._description = description
        self._dataset_id = dataset_id
        self._variable_id = variable_id
        self._url = url
        self._source = source
        self._spatial_resolution = spatial_resolution
        self._temporal_resolution = temporal_resolution
        self._z_meta = z_meta

    @classmethod
    def from_dict(cls, dikt) -> 'MetadataResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The metadata_result of this MetadataResult.  # noqa: E501
        :rtype: MetadataResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this MetadataResult.

        Name of the Dataset  # noqa: E501

        :return: The name of this MetadataResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this MetadataResult.

        Name of the Dataset  # noqa: E501

        :param name: The name of this MetadataResult.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self) -> str:
        """Gets the description of this MetadataResult.


        :return: The description of this MetadataResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this MetadataResult.


        :param description: The description of this MetadataResult.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def dataset_id(self) -> str:
        """Gets the dataset_id of this MetadataResult.

        The id of the dataset or variable within the data location  # noqa: E501

        :return: The dataset_id of this MetadataResult.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id: str):
        """Sets the dataset_id of this MetadataResult.

        The id of the dataset or variable within the data location  # noqa: E501

        :param dataset_id: The dataset_id of this MetadataResult.
        :type dataset_id: str
        """

        self._dataset_id = dataset_id

    @property
    def variable_id(self) -> str:
        """Gets the variable_id of this MetadataResult.

        The variable id searched for  # noqa: E501

        :return: The variable_id of this MetadataResult.
        :rtype: str
        """
        return self._variable_id

    @variable_id.setter
    def variable_id(self, variable_id: str):
        """Sets the variable_id of this MetadataResult.

        The variable id searched for  # noqa: E501

        :param variable_id: The variable_id of this MetadataResult.
        :type variable_id: str
        """

        self._variable_id = variable_id

    @property
    def url(self) -> str:
        """Gets the url of this MetadataResult.


        :return: The url of this MetadataResult.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this MetadataResult.


        :param url: The url of this MetadataResult.
        :type url: str
        """

        self._url = url

    @property
    def source(self) -> str:
        """Gets the source of this MetadataResult.


        :return: The source of this MetadataResult.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this MetadataResult.


        :param source: The source of this MetadataResult.
        :type source: str
        """

        self._source = source

    @property
    def spatial_resolution(self) -> str:
        """Gets the spatial_resolution of this MetadataResult.


        :return: The spatial_resolution of this MetadataResult.
        :rtype: str
        """
        return self._spatial_resolution

    @spatial_resolution.setter
    def spatial_resolution(self, spatial_resolution: str):
        """Sets the spatial_resolution of this MetadataResult.


        :param spatial_resolution: The spatial_resolution of this MetadataResult.
        :type spatial_resolution: str
        """

        self._spatial_resolution = spatial_resolution

    @property
    def temporal_resolution(self) -> str:
        """Gets the temporal_resolution of this MetadataResult.


        :return: The temporal_resolution of this MetadataResult.
        :rtype: str
        """
        return self._temporal_resolution

    @temporal_resolution.setter
    def temporal_resolution(self, temporal_resolution: str):
        """Sets the temporal_resolution of this MetadataResult.


        :param temporal_resolution: The temporal_resolution of this MetadataResult.
        :type temporal_resolution: str
        """

        self._temporal_resolution = temporal_resolution

    @property
    def z_meta(self) -> List[object]:
        """Gets the z_meta of this MetadataResult.


        :return: The z_meta of this MetadataResult.
        :rtype: List[object]
        """
        return self._z_meta

    @z_meta.setter
    def z_meta(self, z_meta: List[object]):
        """Sets the z_meta of this MetadataResult.


        :param z_meta: The z_meta of this MetadataResult.
        :type z_meta: List[object]
        """

        self._z_meta = z_meta
