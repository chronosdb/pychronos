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


class InlineResponse200(object):
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
        'limit': 'float',
        'offset': 'float',
        'total': 'float',
        'result': 'list[Upload]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'total': 'total',
        'result': 'result'
    }

    def __init__(self, limit=None, offset=None, total=None, result=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501

        self._limit = None
        self._offset = None
        self._total = None
        self._result = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total
        if result is not None:
            self.result = result

    @property
    def limit(self):
        """Gets the limit of this InlineResponse200.  # noqa: E501


        :return: The limit of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this InlineResponse200.


        :param limit: The limit of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this InlineResponse200.  # noqa: E501


        :return: The offset of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this InlineResponse200.


        :param offset: The offset of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this InlineResponse200.  # noqa: E501


        :return: The total of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse200.


        :param total: The total of this InlineResponse200.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def result(self):
        """Gets the result of this InlineResponse200.  # noqa: E501


        :return: The result of this InlineResponse200.  # noqa: E501
        :rtype: list[Upload]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse200.


        :param result: The result of this InlineResponse200.  # noqa: E501
        :type: list[Upload]
        """

        self._result = result

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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
