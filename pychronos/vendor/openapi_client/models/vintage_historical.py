# coding: utf-8

"""
    ChronosDB swagger

    ChronosDB time series database API  # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: apiteam@chronosdb.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class VintageHistorical(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'vid': 'str',
        'name': 'str',
        'description': 'str',
        'realtime': 'datetime',
        'tsids': 'list[str]',
        'metadata': 'dict(str, object)',
        'real_start': 'datetime',
        'real_end': 'datetime'
    }

    attribute_map = {
        'vid': 'vid',
        'name': 'name',
        'description': 'description',
        'realtime': 'realtime',
        'tsids': 'tsids',
        'metadata': 'metadata',
        'real_start': 'realStart',
        'real_end': 'realEnd'
    }

    def __init__(self, vid=None, name=None, description=None, realtime=None, tsids=None, metadata=None, real_start=None, real_end=None):  # noqa: E501
        """VintageHistorical - a model defined in OpenAPI"""  # noqa: E501

        self._vid = None
        self._name = None
        self._description = None
        self._realtime = None
        self._tsids = None
        self._metadata = None
        self._real_start = None
        self._real_end = None
        self.discriminator = None

        if vid is not None:
            self.vid = vid
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if realtime is not None:
            self.realtime = realtime
        if tsids is not None:
            self.tsids = tsids
        if metadata is not None:
            self.metadata = metadata
        if real_start is not None:
            self.real_start = real_start
        if real_end is not None:
            self.real_end = real_end

    @property
    def vid(self):
        """Gets the vid of this VintageHistorical.  # noqa: E501


        :return: The vid of this VintageHistorical.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this VintageHistorical.


        :param vid: The vid of this VintageHistorical.  # noqa: E501
        :type: str
        """
        if vid is not None and not re.search(r'[0-9a-fA-F]{24}', vid):  # noqa: E501
            raise ValueError(r"Invalid value for `vid`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._vid = vid

    @property
    def name(self):
        """Gets the name of this VintageHistorical.  # noqa: E501


        :return: The name of this VintageHistorical.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VintageHistorical.


        :param name: The name of this VintageHistorical.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this VintageHistorical.  # noqa: E501


        :return: The description of this VintageHistorical.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VintageHistorical.


        :param description: The description of this VintageHistorical.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def realtime(self):
        """Gets the realtime of this VintageHistorical.  # noqa: E501


        :return: The realtime of this VintageHistorical.  # noqa: E501
        :rtype: datetime
        """
        return self._realtime

    @realtime.setter
    def realtime(self, realtime):
        """Sets the realtime of this VintageHistorical.


        :param realtime: The realtime of this VintageHistorical.  # noqa: E501
        :type: datetime
        """

        self._realtime = realtime

    @property
    def tsids(self):
        """Gets the tsids of this VintageHistorical.  # noqa: E501

        array of time series id, which were saved in this vintage  # noqa: E501

        :return: The tsids of this VintageHistorical.  # noqa: E501
        :rtype: list[str]
        """
        return self._tsids

    @tsids.setter
    def tsids(self, tsids):
        """Sets the tsids of this VintageHistorical.

        array of time series id, which were saved in this vintage  # noqa: E501

        :param tsids: The tsids of this VintageHistorical.  # noqa: E501
        :type: list[str]
        """

        self._tsids = tsids

    @property
    def metadata(self):
        """Gets the metadata of this VintageHistorical.  # noqa: E501


        :return: The metadata of this VintageHistorical.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this VintageHistorical.


        :param metadata: The metadata of this VintageHistorical.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

    @property
    def real_start(self):
        """Gets the real_start of this VintageHistorical.  # noqa: E501

        time when the time series definition is valid from  # noqa: E501

        :return: The real_start of this VintageHistorical.  # noqa: E501
        :rtype: datetime
        """
        return self._real_start

    @real_start.setter
    def real_start(self, real_start):
        """Sets the real_start of this VintageHistorical.

        time when the time series definition is valid from  # noqa: E501

        :param real_start: The real_start of this VintageHistorical.  # noqa: E501
        :type: datetime
        """

        self._real_start = real_start

    @property
    def real_end(self):
        """Gets the real_end of this VintageHistorical.  # noqa: E501

        time when the time series definition is valid until  # noqa: E501

        :return: The real_end of this VintageHistorical.  # noqa: E501
        :rtype: datetime
        """
        return self._real_end

    @real_end.setter
    def real_end(self, real_end):
        """Sets the real_end of this VintageHistorical.

        time when the time series definition is valid until  # noqa: E501

        :param real_end: The real_end of this VintageHistorical.  # noqa: E501
        :type: datetime
        """

        self._real_end = real_end

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VintageHistorical):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
