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


class AnnotationHistorical(object):
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
        'aid': 'str',
        'symbol': 'str',
        'text': 'str',
        'format': 'str',
        'attributes': 'dict(str, object)',
        'targets': 'list[AnnotationTarget]',
        'deleted': 'bool',
        'real_start': 'datetime',
        'real_end': 'datetime'
    }

    attribute_map = {
        'coll_id': 'coll_id',
        'aid': 'aid',
        'symbol': 'symbol',
        'text': 'text',
        'format': 'format',
        'attributes': 'attributes',
        'targets': 'targets',
        'deleted': 'deleted',
        'real_start': 'realStart',
        'real_end': 'realEnd'
    }

    def __init__(self, coll_id=None, aid=None, symbol=None, text=None, format=None, attributes=None, targets=None, deleted=None, real_start=None, real_end=None):  # noqa: E501
        """AnnotationHistorical - a model defined in OpenAPI"""  # noqa: E501

        self._coll_id = None
        self._aid = None
        self._symbol = None
        self._text = None
        self._format = None
        self._attributes = None
        self._targets = None
        self._deleted = None
        self._real_start = None
        self._real_end = None
        self.discriminator = None

        if coll_id is not None:
            self.coll_id = coll_id
        if aid is not None:
            self.aid = aid
        if symbol is not None:
            self.symbol = symbol
        if text is not None:
            self.text = text
        if format is not None:
            self.format = format
        if attributes is not None:
            self.attributes = attributes
        if targets is not None:
            self.targets = targets
        if deleted is not None:
            self.deleted = deleted
        if real_start is not None:
            self.real_start = real_start
        if real_end is not None:
            self.real_end = real_end

    @property
    def coll_id(self):
        """Gets the coll_id of this AnnotationHistorical.  # noqa: E501


        :return: The coll_id of this AnnotationHistorical.  # noqa: E501
        :rtype: str
        """
        return self._coll_id

    @coll_id.setter
    def coll_id(self, coll_id):
        """Sets the coll_id of this AnnotationHistorical.


        :param coll_id: The coll_id of this AnnotationHistorical.  # noqa: E501
        :type: str
        """
        if coll_id is not None and not re.search(r'[0-9a-fA-F]{24}', coll_id):  # noqa: E501
            raise ValueError(r"Invalid value for `coll_id`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._coll_id = coll_id

    @property
    def aid(self):
        """Gets the aid of this AnnotationHistorical.  # noqa: E501


        :return: The aid of this AnnotationHistorical.  # noqa: E501
        :rtype: str
        """
        return self._aid

    @aid.setter
    def aid(self, aid):
        """Sets the aid of this AnnotationHistorical.


        :param aid: The aid of this AnnotationHistorical.  # noqa: E501
        :type: str
        """
        if aid is not None and not re.search(r'[0-9a-fA-F]{24}', aid):  # noqa: E501
            raise ValueError(r"Invalid value for `aid`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._aid = aid

    @property
    def symbol(self):
        """Gets the symbol of this AnnotationHistorical.  # noqa: E501

        annotation symbol  # noqa: E501

        :return: The symbol of this AnnotationHistorical.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this AnnotationHistorical.

        annotation symbol  # noqa: E501

        :param symbol: The symbol of this AnnotationHistorical.  # noqa: E501
        :type: str
        """
        if symbol is not None and not re.search(r'^[0-9a-zA-Z]{1,10}$', symbol):  # noqa: E501
            raise ValueError(r"Invalid value for `symbol`, must be a follow pattern or equal to `/^[0-9a-zA-Z]{1,10}$/`")  # noqa: E501

        self._symbol = symbol

    @property
    def text(self):
        """Gets the text of this AnnotationHistorical.  # noqa: E501


        :return: The text of this AnnotationHistorical.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this AnnotationHistorical.


        :param text: The text of this AnnotationHistorical.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def format(self):
        """Gets the format of this AnnotationHistorical.  # noqa: E501


        :return: The format of this AnnotationHistorical.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this AnnotationHistorical.


        :param format: The format of this AnnotationHistorical.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def attributes(self):
        """Gets the attributes of this AnnotationHistorical.  # noqa: E501

        json-type object can be added to annotation to store some extra data or metadata  # noqa: E501

        :return: The attributes of this AnnotationHistorical.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this AnnotationHistorical.

        json-type object can be added to annotation to store some extra data or metadata  # noqa: E501

        :param attributes: The attributes of this AnnotationHistorical.  # noqa: E501
        :type: dict(str, object)
        """

        self._attributes = attributes

    @property
    def targets(self):
        """Gets the targets of this AnnotationHistorical.  # noqa: E501

        annotated targets  # noqa: E501

        :return: The targets of this AnnotationHistorical.  # noqa: E501
        :rtype: list[AnnotationTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this AnnotationHistorical.

        annotated targets  # noqa: E501

        :param targets: The targets of this AnnotationHistorical.  # noqa: E501
        :type: list[AnnotationTarget]
        """

        self._targets = targets

    @property
    def deleted(self):
        """Gets the deleted of this AnnotationHistorical.  # noqa: E501

        time when the time series definition is valid from  # noqa: E501

        :return: The deleted of this AnnotationHistorical.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this AnnotationHistorical.

        time when the time series definition is valid from  # noqa: E501

        :param deleted: The deleted of this AnnotationHistorical.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def real_start(self):
        """Gets the real_start of this AnnotationHistorical.  # noqa: E501

        time when the time series definition is valid from  # noqa: E501

        :return: The real_start of this AnnotationHistorical.  # noqa: E501
        :rtype: datetime
        """
        return self._real_start

    @real_start.setter
    def real_start(self, real_start):
        """Sets the real_start of this AnnotationHistorical.

        time when the time series definition is valid from  # noqa: E501

        :param real_start: The real_start of this AnnotationHistorical.  # noqa: E501
        :type: datetime
        """

        self._real_start = real_start

    @property
    def real_end(self):
        """Gets the real_end of this AnnotationHistorical.  # noqa: E501

        time when the time series definition is valid until  # noqa: E501

        :return: The real_end of this AnnotationHistorical.  # noqa: E501
        :rtype: datetime
        """
        return self._real_end

    @real_end.setter
    def real_end(self, real_end):
        """Sets the real_end of this AnnotationHistorical.

        time when the time series definition is valid until  # noqa: E501

        :param real_end: The real_end of this AnnotationHistorical.  # noqa: E501
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
        if not isinstance(other, AnnotationHistorical):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other