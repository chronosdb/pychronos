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


class CollectionPermission(object):
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
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'email': 'str',
        'role': 'str',
        'effect': 'str'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'email': 'email',
        'role': 'role',
        'effect': 'effect'
    }

    def __init__(self, type=None, id=None, name=None, email=None, role=None, effect=None):  # noqa: E501
        """CollectionPermission - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._id = None
        self._name = None
        self._email = None
        self._role = None
        self._effect = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        if role is not None:
            self.role = role
        if effect is not None:
            self.effect = effect

    @property
    def type(self):
        """Gets the type of this CollectionPermission.  # noqa: E501

        member type: `g` group `u` user   # noqa: E501

        :return: The type of this CollectionPermission.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CollectionPermission.

        member type: `g` group `u` user   # noqa: E501

        :param type: The type of this CollectionPermission.  # noqa: E501
        :type: str
        """
        allowed_values = ["g", "u"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def id(self):
        """Gets the id of this CollectionPermission.  # noqa: E501


        :return: The id of this CollectionPermission.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CollectionPermission.


        :param id: The id of this CollectionPermission.  # noqa: E501
        :type: str
        """
        if id is not None and not re.search(r'[0-9a-fA-F]{24}', id):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this CollectionPermission.  # noqa: E501

        username or groupname  # noqa: E501

        :return: The name of this CollectionPermission.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CollectionPermission.

        username or groupname  # noqa: E501

        :param name: The name of this CollectionPermission.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this CollectionPermission.  # noqa: E501

        email  # noqa: E501

        :return: The email of this CollectionPermission.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CollectionPermission.

        email  # noqa: E501

        :param email: The email of this CollectionPermission.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def role(self):
        """Gets the role of this CollectionPermission.  # noqa: E501

        roles: `annotator` space member, who can annotate data `uploader` space member, who can write data `analyst` space member, who can read/write data, read members `maintainer` space maintainer, who can add/remove members, and edit space info   # noqa: E501

        :return: The role of this CollectionPermission.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this CollectionPermission.

        roles: `annotator` space member, who can annotate data `uploader` space member, who can write data `analyst` space member, who can read/write data, read members `maintainer` space maintainer, who can add/remove members, and edit space info   # noqa: E501

        :param role: The role of this CollectionPermission.  # noqa: E501
        :type: str
        """
        allowed_values = ["annotator", "uploader", "analyst", "maintainer"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def effect(self):
        """Gets the effect of this CollectionPermission.  # noqa: E501


        :return: The effect of this CollectionPermission.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this CollectionPermission.


        :param effect: The effect of this CollectionPermission.  # noqa: E501
        :type: str
        """
        allowed_values = ["allow", "deny"]  # noqa: E501
        if effect not in allowed_values:
            raise ValueError(
                "Invalid value for `effect` ({0}), must be one of {1}"  # noqa: E501
                .format(effect, allowed_values)
            )

        self._effect = effect

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
        if not isinstance(other, CollectionPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
