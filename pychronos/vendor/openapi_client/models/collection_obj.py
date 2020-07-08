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


class CollectionObj(object):
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
        'coll_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'coll_id': 'coll_id',
        'name': 'name'
    }

    def __init__(self, coll_id=None, name=None):  # noqa: E501
        """CollectionObj - a model defined in OpenAPI"""  # noqa: E501

        self._coll_id = None
        self._name = None
        self.discriminator = None

        self.coll_id = coll_id
        self.name = name

    @property
    def coll_id(self):
        """Gets the coll_id of this CollectionObj.  # noqa: E501


        :return: The coll_id of this CollectionObj.  # noqa: E501
        :rtype: str
        """
        return self._coll_id

    @coll_id.setter
    def coll_id(self, coll_id):
        """Sets the coll_id of this CollectionObj.


        :param coll_id: The coll_id of this CollectionObj.  # noqa: E501
        :type: str
        """
        if coll_id is None:
            raise ValueError("Invalid value for `coll_id`, must not be `None`")  # noqa: E501
        if coll_id is not None and not re.search(r'[0-9a-fA-F]{24}', coll_id):  # noqa: E501
            raise ValueError(r"Invalid value for `coll_id`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._coll_id = coll_id

    @property
    def name(self):
        """Gets the name of this CollectionObj.  # noqa: E501


        :return: The name of this CollectionObj.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CollectionObj.


        :param name: The name of this CollectionObj.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{4,59}$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{4,59}$/`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, CollectionObj):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other