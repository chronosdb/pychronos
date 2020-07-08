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


class GroupHistorical(object):
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
        'email': 'str',
        'description': 'str',
        'organization': 'str',
        'location': 'str',
        'website': 'str',
        'visibility': 'Visibility',
        'members': 'list[Member]',
        'deleted': 'bool',
        'real_start': 'datetime',
        'real_end': 'datetime'
    }

    attribute_map = {
        'gid': 'gid',
        'groupname': 'groupname',
        'email': 'email',
        'description': 'description',
        'organization': 'organization',
        'location': 'location',
        'website': 'website',
        'visibility': 'visibility',
        'members': 'members',
        'deleted': 'deleted',
        'real_start': 'realStart',
        'real_end': 'realEnd'
    }

    def __init__(self, gid=None, groupname=None, email=None, description=None, organization=None, location=None, website=None, visibility=None, members=None, deleted=None, real_start=None, real_end=None):  # noqa: E501
        """GroupHistorical - a model defined in OpenAPI"""  # noqa: E501

        self._gid = None
        self._groupname = None
        self._email = None
        self._description = None
        self._organization = None
        self._location = None
        self._website = None
        self._visibility = None
        self._members = None
        self._deleted = None
        self._real_start = None
        self._real_end = None
        self.discriminator = None

        if gid is not None:
            self.gid = gid
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
        if members is not None:
            self.members = members
        if deleted is not None:
            self.deleted = deleted
        if real_start is not None:
            self.real_start = real_start
        if real_end is not None:
            self.real_end = real_end

    @property
    def gid(self):
        """Gets the gid of this GroupHistorical.  # noqa: E501


        :return: The gid of this GroupHistorical.  # noqa: E501
        :rtype: str
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this GroupHistorical.


        :param gid: The gid of this GroupHistorical.  # noqa: E501
        :type: str
        """
        if gid is not None and not re.search(r'[0-9a-fA-F]{24}', gid):  # noqa: E501
            raise ValueError(r"Invalid value for `gid`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._gid = gid

    @property
    def groupname(self):
        """Gets the groupname of this GroupHistorical.  # noqa: E501


        :return: The groupname of this GroupHistorical.  # noqa: E501
        :rtype: str
        """
        return self._groupname

    @groupname.setter
    def groupname(self, groupname):
        """Sets the groupname of this GroupHistorical.


        :param groupname: The groupname of this GroupHistorical.  # noqa: E501
        :type: str
        """
        if groupname is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{4,59}$', groupname):  # noqa: E501
            raise ValueError(r"Invalid value for `groupname`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{4,59}$/`")  # noqa: E501

        self._groupname = groupname

    @property
    def email(self):
        """Gets the email of this GroupHistorical.  # noqa: E501


        :return: The email of this GroupHistorical.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GroupHistorical.


        :param email: The email of this GroupHistorical.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def description(self):
        """Gets the description of this GroupHistorical.  # noqa: E501


        :return: The description of this GroupHistorical.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupHistorical.


        :param description: The description of this GroupHistorical.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def organization(self):
        """Gets the organization of this GroupHistorical.  # noqa: E501


        :return: The organization of this GroupHistorical.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this GroupHistorical.


        :param organization: The organization of this GroupHistorical.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def location(self):
        """Gets the location of this GroupHistorical.  # noqa: E501


        :return: The location of this GroupHistorical.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this GroupHistorical.


        :param location: The location of this GroupHistorical.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def website(self):
        """Gets the website of this GroupHistorical.  # noqa: E501


        :return: The website of this GroupHistorical.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this GroupHistorical.


        :param website: The website of this GroupHistorical.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def visibility(self):
        """Gets the visibility of this GroupHistorical.  # noqa: E501


        :return: The visibility of this GroupHistorical.  # noqa: E501
        :rtype: Visibility
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this GroupHistorical.


        :param visibility: The visibility of this GroupHistorical.  # noqa: E501
        :type: Visibility
        """

        self._visibility = visibility

    @property
    def members(self):
        """Gets the members of this GroupHistorical.  # noqa: E501


        :return: The members of this GroupHistorical.  # noqa: E501
        :rtype: list[Member]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this GroupHistorical.


        :param members: The members of this GroupHistorical.  # noqa: E501
        :type: list[Member]
        """

        self._members = members

    @property
    def deleted(self):
        """Gets the deleted of this GroupHistorical.  # noqa: E501

        time when the time series definition is valid from  # noqa: E501

        :return: The deleted of this GroupHistorical.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this GroupHistorical.

        time when the time series definition is valid from  # noqa: E501

        :param deleted: The deleted of this GroupHistorical.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def real_start(self):
        """Gets the real_start of this GroupHistorical.  # noqa: E501

        time when the time series definition is valid from  # noqa: E501

        :return: The real_start of this GroupHistorical.  # noqa: E501
        :rtype: datetime
        """
        return self._real_start

    @real_start.setter
    def real_start(self, real_start):
        """Sets the real_start of this GroupHistorical.

        time when the time series definition is valid from  # noqa: E501

        :param real_start: The real_start of this GroupHistorical.  # noqa: E501
        :type: datetime
        """

        self._real_start = real_start

    @property
    def real_end(self):
        """Gets the real_end of this GroupHistorical.  # noqa: E501

        time when the time series definition is valid until  # noqa: E501

        :return: The real_end of this GroupHistorical.  # noqa: E501
        :rtype: datetime
        """
        return self._real_end

    @real_end.setter
    def real_end(self, real_end):
        """Sets the real_end of this GroupHistorical.

        time when the time series definition is valid until  # noqa: E501

        :param real_end: The real_end of this GroupHistorical.  # noqa: E501
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
        if not isinstance(other, GroupHistorical):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other