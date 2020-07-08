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


class RawDataDeleteResponse(object):
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
        'tsid': 'str',
        'realtime': 'datetime'
    }

    attribute_map = {
        'coll_id': 'collId',
        'tsid': 'tsid',
        'realtime': 'realtime'
    }

    def __init__(self, coll_id=None, tsid=None, realtime=None):  # noqa: E501
        """RawDataDeleteResponse - a model defined in OpenAPI"""  # noqa: E501

        self._coll_id = None
        self._tsid = None
        self._realtime = None
        self.discriminator = None

        if coll_id is not None:
            self.coll_id = coll_id
        if tsid is not None:
            self.tsid = tsid
        if realtime is not None:
            self.realtime = realtime

    @property
    def coll_id(self):
        """Gets the coll_id of this RawDataDeleteResponse.  # noqa: E501


        :return: The coll_id of this RawDataDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._coll_id

    @coll_id.setter
    def coll_id(self, coll_id):
        """Sets the coll_id of this RawDataDeleteResponse.


        :param coll_id: The coll_id of this RawDataDeleteResponse.  # noqa: E501
        :type: str
        """
        if coll_id is not None and not re.search(r'[0-9a-fA-F]{24}', coll_id):  # noqa: E501
            raise ValueError(r"Invalid value for `coll_id`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._coll_id = coll_id

    @property
    def tsid(self):
        """Gets the tsid of this RawDataDeleteResponse.  # noqa: E501


        :return: The tsid of this RawDataDeleteResponse.  # noqa: E501
        :rtype: str
        """
        return self._tsid

    @tsid.setter
    def tsid(self, tsid):
        """Sets the tsid of this RawDataDeleteResponse.


        :param tsid: The tsid of this RawDataDeleteResponse.  # noqa: E501
        :type: str
        """
        if tsid is not None and not re.search(r'[0-9a-fA-F]{24}', tsid):  # noqa: E501
            raise ValueError(r"Invalid value for `tsid`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._tsid = tsid

    @property
    def realtime(self):
        """Gets the realtime of this RawDataDeleteResponse.  # noqa: E501

        realtime until when the observations are valid  # noqa: E501

        :return: The realtime of this RawDataDeleteResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._realtime

    @realtime.setter
    def realtime(self, realtime):
        """Sets the realtime of this RawDataDeleteResponse.

        realtime until when the observations are valid  # noqa: E501

        :param realtime: The realtime of this RawDataDeleteResponse.  # noqa: E501
        :type: datetime
        """

        self._realtime = realtime

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
        if not isinstance(other, RawDataDeleteResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
