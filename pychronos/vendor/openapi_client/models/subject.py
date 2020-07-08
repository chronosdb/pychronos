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


class Subject(object):
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
        'type': 'SubjectType',
        'user': 'UserSummary',
        'group': 'GroupSummary'
    }

    attribute_map = {
        'type': 'type',
        'user': 'user',
        'group': 'group'
    }

    def __init__(self, type=None, user=None, group=None):  # noqa: E501
        """Subject - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._user = None
        self._group = None
        self.discriminator = None

        self.type = type
        if user is not None:
            self.user = user
        if group is not None:
            self.group = group

    @property
    def type(self):
        """Gets the type of this Subject.  # noqa: E501


        :return: The type of this Subject.  # noqa: E501
        :rtype: SubjectType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subject.


        :param type: The type of this Subject.  # noqa: E501
        :type: SubjectType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def user(self):
        """Gets the user of this Subject.  # noqa: E501


        :return: The user of this Subject.  # noqa: E501
        :rtype: UserSummary
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Subject.


        :param user: The user of this Subject.  # noqa: E501
        :type: UserSummary
        """

        self._user = user

    @property
    def group(self):
        """Gets the group of this Subject.  # noqa: E501


        :return: The group of this Subject.  # noqa: E501
        :rtype: GroupSummary
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Subject.


        :param group: The group of this Subject.  # noqa: E501
        :type: GroupSummary
        """

        self._group = group

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
        if not isinstance(other, Subject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
