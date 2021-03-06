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


class GroupUpdate(object):
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
        'groupname': 'str',
        'email': 'str',
        'description': 'str',
        'organization': 'str',
        'location': 'str',
        'website': 'str',
        'visibility': 'Visibility'
    }

    attribute_map = {
        'groupname': 'groupname',
        'email': 'email',
        'description': 'description',
        'organization': 'organization',
        'location': 'location',
        'website': 'website',
        'visibility': 'visibility'
    }

    def __init__(self, groupname=None, email=None, description=None, organization=None, location=None, website=None, visibility=None):  # noqa: E501
        """GroupUpdate - a model defined in OpenAPI"""  # noqa: E501

        self._groupname = None
        self._email = None
        self._description = None
        self._organization = None
        self._location = None
        self._website = None
        self._visibility = None
        self.discriminator = None

        if groupname is not None:
            self.groupname = groupname
        if email is not None:
            self.email = email
        if description is not None:
            self.description = description
        if organization is not None:
            self.organization = organization
        if location is not None:
            self.location = location
        if website is not None:
            self.website = website
        if visibility is not None:
            self.visibility = visibility

    @property
    def groupname(self):
        """Gets the groupname of this GroupUpdate.  # noqa: E501


        :return: The groupname of this GroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this GroupUpdate.


        :param groupname: The groupname of this GroupUpdate.  # noqa: E501
        :type: str
        """

        self._groupname = groupname

    @property
    def email(self):
        """Gets the email of this GroupUpdate.  # noqa: E501


        :return: The email of this GroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GroupUpdate.


        :param email: The email of this GroupUpdate.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def description(self):
        """Gets the description of this GroupUpdate.  # noqa: E501


        :return: The description of this GroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupUpdate.


        :param description: The description of this GroupUpdate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization(self):
        """Gets the organization of this GroupUpdate.  # noqa: E501


        :return: The organization of this GroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this GroupUpdate.


        :param organization: The organization of this GroupUpdate.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def location(self):
        """Gets the location of this GroupUpdate.  # noqa: E501


        :return: The location of this GroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GroupUpdate.


        :param location: The location of this GroupUpdate.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def website(self):
        """Gets the website of this GroupUpdate.  # noqa: E501


        :return: The website of this GroupUpdate.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this GroupUpdate.


        :param website: The website of this GroupUpdate.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def visibility(self):
        """Gets the visibility of this GroupUpdate.  # noqa: E501


        :return: The visibility of this GroupUpdate.  # noqa: E501
        :rtype: Visibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GroupUpdate.


        :param visibility: The visibility of this GroupUpdate.  # noqa: E501
        :type: Visibility
        """

        self._visibility = visibility

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
        if not isinstance(other, GroupUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
