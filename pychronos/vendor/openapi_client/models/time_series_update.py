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


class TimeSeriesUpdate(object):
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
        'name': 'str',
        'unit': 'object',
        'title': 'str',
        'description': 'str',
        'discontinued': 'bool',
        'legend': 'object',
        'attributes': 'object'
    }

    attribute_map = {
        'name': 'name',
        'unit': 'unit',
        'title': 'title',
        'description': 'description',
        'discontinued': 'discontinued',
        'legend': 'legend',
        'attributes': 'attributes'
    }

    def __init__(self, name=None, unit=None, title=None, description=None, discontinued=None, legend=None, attributes=None):  # noqa: E501
        """TimeSeriesUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._unit = None
        self._title = None
        self._description = None
        self._discontinued = None
        self._legend = None
        self._attributes = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if unit is not None:
            self.unit = unit
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if discontinued is not None:
            self.discontinued = discontinued
        if legend is not None:
            self.legend = legend
        if attributes is not None:
            self.attributes = attributes

    @property
    def name(self):
        """Gets the name of this TimeSeriesUpdate.  # noqa: E501

        unique series name in a collection  # noqa: E501

        :return: The name of this TimeSeriesUpdate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimeSeriesUpdate.

        unique series name in a collection  # noqa: E501

        :param name: The name of this TimeSeriesUpdate.  # noqa: E501
        :type: str
        """
        if name is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{0,59}$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{0,59}$/`")  # noqa: E501

        self._name = name

    @property
    def unit(self):
        """Gets the unit of this TimeSeriesUpdate.  # noqa: E501

        units of values  # noqa: E501

        :return: The unit of this TimeSeriesUpdate.  # noqa: E501
        :rtype: object
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TimeSeriesUpdate.

        units of values  # noqa: E501

        :param unit: The unit of this TimeSeriesUpdate.  # noqa: E501
        :type: object
        """

        self._unit = unit

    @property
    def title(self):
        """Gets the title of this TimeSeriesUpdate.  # noqa: E501

        Title of time series  # noqa: E501

        :return: The title of this TimeSeriesUpdate.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TimeSeriesUpdate.

        Title of time series  # noqa: E501

        :param title: The title of this TimeSeriesUpdate.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this TimeSeriesUpdate.  # noqa: E501

        Detail description of time series  # noqa: E501

        :return: The description of this TimeSeriesUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TimeSeriesUpdate.

        Detail description of time series  # noqa: E501

        :param description: The description of this TimeSeriesUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def discontinued(self):
        """Gets the discontinued of this TimeSeriesUpdate.  # noqa: E501

        Time series, which are no longer recorded can be marked as discontinued. Discontinued series can be kept in the database for historical reasons  # noqa: E501

        :return: The discontinued of this TimeSeriesUpdate.  # noqa: E501
        :rtype: bool
        """
        return self._discontinued

    @discontinued.setter
    def discontinued(self, discontinued):
        """Sets the discontinued of this TimeSeriesUpdate.

        Time series, which are no longer recorded can be marked as discontinued. Discontinued series can be kept in the database for historical reasons  # noqa: E501

        :param discontinued: The discontinued of this TimeSeriesUpdate.  # noqa: E501
        :type: bool
        """

        self._discontinued = discontinued

    @property
    def legend(self):
        """Gets the legend of this TimeSeriesUpdate.  # noqa: E501

        Legend for observation status; it maps integer to a status string, e.g. 1 -> preliminary, 2-> projected, etc.  # noqa: E501

        :return: The legend of this TimeSeriesUpdate.  # noqa: E501
        :rtype: object
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this TimeSeriesUpdate.

        Legend for observation status; it maps integer to a status string, e.g. 1 -> preliminary, 2-> projected, etc.  # noqa: E501

        :param legend: The legend of this TimeSeriesUpdate.  # noqa: E501
        :type: object
        """

        self._legend = legend

    @property
    def attributes(self):
        """Gets the attributes of this TimeSeriesUpdate.  # noqa: E501

        Time series attributes are key-value pairs used to store meta information about the series, e.g. location, region, category, etc. Note that units and discontinued properties are explicitly   # noqa: E501

        :return: The attributes of this TimeSeriesUpdate.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this TimeSeriesUpdate.

        Time series attributes are key-value pairs used to store meta information about the series, e.g. location, region, category, etc. Note that units and discontinued properties are explicitly   # noqa: E501

        :param attributes: The attributes of this TimeSeriesUpdate.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

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
        if not isinstance(other, TimeSeriesUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
