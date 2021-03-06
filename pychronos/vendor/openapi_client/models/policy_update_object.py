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


class PolicyUpdateObject(object):
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
        'type': 'ObjectType',
        'space_id': 'str',
        'coll_id': 'str',
        'tsid': 'str',
        'subobject': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'space_id': 'space_id',
        'coll_id': 'coll_id',
        'tsid': 'tsid',
        'subobject': 'subobject'
    }

    def __init__(self, type=None, space_id=None, coll_id=None, tsid=None, subobject=None):  # noqa: E501
        """PolicyUpdateObject - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._space_id = None
        self._coll_id = None
        self._tsid = None
        self._subobject = None
        self.discriminator = None

        self.type = type
        if space_id is not None:
            self.space_id = space_id
        if coll_id is not None:
            self.coll_id = coll_id
        if tsid is not None:
            self.tsid = tsid
        self.subobject = subobject

    @property
    def type(self):
        """Gets the type of this PolicyUpdateObject.  # noqa: E501


        :return: The type of this PolicyUpdateObject.  # noqa: E501
        :rtype: ObjectType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyUpdateObject.


        :param type: The type of this PolicyUpdateObject.  # noqa: E501
        :type: ObjectType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def space_id(self):
        """Gets the space_id of this PolicyUpdateObject.  # noqa: E501


        :return: The space_id of this PolicyUpdateObject.  # noqa: E501
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this PolicyUpdateObject.


        :param space_id: The space_id of this PolicyUpdateObject.  # noqa: E501
        :type: str
        """
        if space_id is not None and not re.search(r'[0-9a-fA-F]{24}', space_id):  # noqa: E501
            raise ValueError(r"Invalid value for `space_id`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._space_id = space_id

    @property
    def coll_id(self):
        """Gets the coll_id of this PolicyUpdateObject.  # noqa: E501


        :return: The coll_id of this PolicyUpdateObject.  # noqa: E501
        :rtype: str
        """
        return self._coll_id

    @coll_id.setter
    def coll_id(self, coll_id):
        """Sets the coll_id of this PolicyUpdateObject.


        :param coll_id: The coll_id of this PolicyUpdateObject.  # noqa: E501
        :type: str
        """
        if coll_id is not None and not re.search(r'[0-9a-fA-F]{24}', coll_id):  # noqa: E501
            raise ValueError(r"Invalid value for `coll_id`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._coll_id = coll_id

    @property
    def tsid(self):
        """Gets the tsid of this PolicyUpdateObject.  # noqa: E501


        :return: The tsid of this PolicyUpdateObject.  # noqa: E501
        :rtype: str
        """
        return self._tsid

    @tsid.setter
    def tsid(self, tsid):
        """Sets the tsid of this PolicyUpdateObject.


        :param tsid: The tsid of this PolicyUpdateObject.  # noqa: E501
        :type: str
        """
        if tsid is not None and not re.search(r'[0-9a-fA-F]{24}', tsid):  # noqa: E501
            raise ValueError(r"Invalid value for `tsid`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._tsid = tsid

    @property
    def subobject(self):
        """Gets the subobject of this PolicyUpdateObject.  # noqa: E501


        :return: The subobject of this PolicyUpdateObject.  # noqa: E501
        :rtype: bool
        """
        return self._subobject

    @subobject.setter
    def subobject(self, subobject):
        """Sets the subobject of this PolicyUpdateObject.


        :param subobject: The subobject of this PolicyUpdateObject.  # noqa: E501
        :type: bool
        """
        if subobject is None:
            raise ValueError("Invalid value for `subobject`, must not be `None`")  # noqa: E501

        self._subobject = subobject

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
        if not isinstance(other, PolicyUpdateObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
