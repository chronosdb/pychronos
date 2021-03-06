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


class TimeSeriesSummaryAllOf(object):
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
        'title': 'str',
        'discontinued': 'bool',
        'unit': 'object'
    }

    attribute_map = {
        'title': 'title',
        'discontinued': 'discontinued',
        'unit': 'unit'
    }

    def __init__(self, title=None, discontinued=None, unit=None):  # noqa: E501
        """TimeSeriesSummaryAllOf - a model defined in OpenAPI"""  # noqa: E501

        self._title = None
        self._discontinued = None
        self._unit = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if discontinued is not None:
            self.discontinued = discontinued
        if unit is not None:
            self.unit = unit

    @property
    def title(self):
        """Gets the title of this TimeSeriesSummaryAllOf.  # noqa: E501

        Title of time series  # noqa: E501

        :return: The title of this TimeSeriesSummaryAllOf.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TimeSeriesSummaryAllOf.

        Title of time series  # noqa: E501

        :param title: The title of this TimeSeriesSummaryAllOf.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def discontinued(self):
        """Gets the discontinued of this TimeSeriesSummaryAllOf.  # noqa: E501

        Time series, which are no longer recorded can be marked as discontinued. Discontinued series can be kept in the database for historical reasons  # noqa: E501

        :return: The discontinued of this TimeSeriesSummaryAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._discontinued

    @discontinued.setter
    def discontinued(self, discontinued):
        """Sets the discontinued of this TimeSeriesSummaryAllOf.

        Time series, which are no longer recorded can be marked as discontinued. Discontinued series can be kept in the database for historical reasons  # noqa: E501

        :param discontinued: The discontinued of this TimeSeriesSummaryAllOf.  # noqa: E501
        :type: bool
        """

        self._discontinued = discontinued

    @property
    def unit(self):
        """Gets the unit of this TimeSeriesSummaryAllOf.  # noqa: E501

        units of values  # noqa: E501

        :return: The unit of this TimeSeriesSummaryAllOf.  # noqa: E501
        :rtype: object
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TimeSeriesSummaryAllOf.

        units of values  # noqa: E501

        :param unit: The unit of this TimeSeriesSummaryAllOf.  # noqa: E501
        :type: object
        """

        self._unit = unit

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
        if not isinstance(other, TimeSeriesSummaryAllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
