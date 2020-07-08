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


class GroupSummary(object):
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
        'gid': 'str',
        'groupname': 'str',
        'email': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'groupname': 'groupname',
        'email': 'email'
    }

    def __init__(self, gid=None, groupname=None, email=None):  # noqa: E501
        """GroupSummary - a model defined in OpenAPI"""  # noqa: E501

        self._gid = None
        self._groupname = None
        self._email = None
        self.discriminator = None

        if gid is not None:
            self.gid = gid
        if groupname is not None:
            self.groupname = groupname
        if email is not None:
            self.email = email

    @property
    def gid(self):
        """Gets the gid of this GroupSummary.  # noqa: E501


        :return: The gid of this GroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this GroupSummary.


        :param gid: The gid of this GroupSummary.  # noqa: E501
        :type: str
        """
        if gid is not None and not re.search(r'[0-9a-fA-F]{24}', gid):  # noqa: E501
            raise ValueError(r"Invalid value for `gid`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._gid = gid

    @property
    def groupname(self):
        """Gets the groupname of this GroupSummary.  # noqa: E501


        :return: The groupname of this GroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this GroupSummary.


        :param groupname: The groupname of this GroupSummary.  # noqa: E501
        :type: str
        """

        self._groupname = groupname

    @property
    def email(self):
        """Gets the email of this GroupSummary.  # noqa: E501


        :return: The email of this GroupSummary.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GroupSummary.


        :param email: The email of this GroupSummary.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if not isinstance(other, GroupSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
