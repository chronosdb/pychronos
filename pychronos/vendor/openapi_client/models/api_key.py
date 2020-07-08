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


class APIKey(object):
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
        'key': 'str',
        'prefix': 'str',
        'scopes': 'list[str]',
        'created_on': 'datetime',
        'expiries_on': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'key': 'key',
        'prefix': 'prefix',
        'scopes': 'scopes',
        'created_on': 'createdOn',
        'expiries_on': 'expiriesOn'
    }

    def __init__(self, name=None, key=None, prefix=None, scopes=None, created_on=None, expiries_on=None):  # noqa: E501
        """APIKey - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._key = None
        self._prefix = None
        self._scopes = None
        self._created_on = None
        self._expiries_on = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.key = key
        if prefix is not None:
            self.prefix = prefix
        if scopes is not None:
            self.scopes = scopes
        if created_on is not None:
            self.created_on = created_on
        self.expiries_on = expiries_on

    @property
    def name(self):
        """Gets the name of this APIKey.  # noqa: E501


        :return: The name of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this APIKey.


        :param name: The name of this APIKey.  # noqa: E501
        :type: str
        """
        if name is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{0,59}$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{0,59}$/`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this APIKey.  # noqa: E501


        :return: The key of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this APIKey.


        :param key: The key of this APIKey.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def prefix(self):
        """Gets the prefix of this APIKey.  # noqa: E501


        :return: The prefix of this APIKey.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this APIKey.


        :param prefix: The prefix of this APIKey.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def scopes(self):
        """Gets the scopes of this APIKey.  # noqa: E501


        :return: The scopes of this APIKey.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this APIKey.


        :param scopes: The scopes of this APIKey.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def created_on(self):
        """Gets the created_on of this APIKey.  # noqa: E501


        :return: The created_on of this APIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this APIKey.


        :param created_on: The created_on of this APIKey.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def expiries_on(self):
        """Gets the expiries_on of this APIKey.  # noqa: E501


        :return: The expiries_on of this APIKey.  # noqa: E501
        :rtype: datetime
        """
        return self._expiries_on

    @expiries_on.setter
    def expiries_on(self, expiries_on):
        """Sets the expiries_on of this APIKey.


        :param expiries_on: The expiries_on of this APIKey.  # noqa: E501
        :type: datetime
        """

        self._expiries_on = expiries_on

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
        if not isinstance(other, APIKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other