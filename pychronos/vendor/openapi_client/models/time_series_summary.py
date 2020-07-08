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


class TimeSeriesSummary(object):
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
        'tsid': 'str',
        'coll_id': 'str',
        'dtype': 'DType',
        'dparams': 'object',
        'itype': 'IType',
        'freq': 'Frequency',
        'fparams': 'object',
        'entity': 'int',
        'variable': 'str',
        'tsi': 'str',
        'space': 'str',
        'collection': 'str',
        'name': 'str',
        'title': 'str',
        'discontinued': 'bool',
        'unit': 'object'
    }

    attribute_map = {
        'tsid': 'tsid',
        'coll_id': 'collId',
        'dtype': 'dtype',
        'dparams': 'dparams',
        'itype': 'itype',
        'freq': 'freq',
        'fparams': 'fparams',
        'entity': 'entity',
        'variable': 'variable',
        'tsi': 'tsi',
        'space': 'space',
        'collection': 'collection',
        'name': 'name',
        'title': 'title',
        'discontinued': 'discontinued',
        'unit': 'unit'
    }

    def __init__(self, tsid=None, coll_id=None, dtype=None, dparams=None, itype=None, freq=None, fparams=None, entity=None, variable=None, tsi=None, space=None, collection=None, name=None, title=None, discontinued=None, unit=None):  # noqa: E501
        """TimeSeriesSummary - a model defined in OpenAPI"""  # noqa: E501

        self._tsid = None
        self._coll_id = None
        self._dtype = None
        self._dparams = None
        self._itype = None
        self._freq = None
        self._fparams = None
        self._entity = None
        self._variable = None
        self._tsi = None
        self._space = None
        self._collection = None
        self._name = None
        self._title = None
        self._discontinued = None
        self._unit = None
        self.discriminator = None

        if tsid is not None:
            self.tsid = tsid
        if coll_id is not None:
            self.coll_id = coll_id
        if dtype is not None:
            self.dtype = dtype
        if dparams is not None:
            self.dparams = dparams
        if itype is not None:
            self.itype = itype
        if freq is not None:
            self.freq = freq
        if fparams is not None:
            self.fparams = fparams
        if entity is not None:
            self.entity = entity
        if variable is not None:
            self.variable = variable
        if tsi is not None:
            self.tsi = tsi
        if space is not None:
            self.space = space
        if collection is not None:
            self.collection = collection
        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if discontinued is not None:
            self.discontinued = discontinued
        if unit is not None:
            self.unit = unit

    @property
    def tsid(self):
        """Gets the tsid of this TimeSeriesSummary.  # noqa: E501


        :return: The tsid of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._tsid

    @tsid.setter
    def tsid(self, tsid):
        """Sets the tsid of this TimeSeriesSummary.


        :param tsid: The tsid of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """
        if tsid is not None and not re.search(r'[0-9a-fA-F]{24}', tsid):  # noqa: E501
            raise ValueError(r"Invalid value for `tsid`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._tsid = tsid

    @property
    def coll_id(self):
        """Gets the coll_id of this TimeSeriesSummary.  # noqa: E501


        :return: The coll_id of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._coll_id

    @coll_id.setter
    def coll_id(self, coll_id):
        """Sets the coll_id of this TimeSeriesSummary.


        :param coll_id: The coll_id of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """
        if coll_id is not None and not re.search(r'[0-9a-fA-F]{24}', coll_id):  # noqa: E501
            raise ValueError(r"Invalid value for `coll_id`, must be a follow pattern or equal to `/[0-9a-fA-F]{24}/`")  # noqa: E501

        self._coll_id = coll_id

    @property
    def dtype(self):
        """Gets the dtype of this TimeSeriesSummary.  # noqa: E501


        :return: The dtype of this TimeSeriesSummary.  # noqa: E501
        :rtype: DType
        """
        return self._dtype

    @dtype.setter
    def dtype(self, dtype):
        """Sets the dtype of this TimeSeriesSummary.


        :param dtype: The dtype of this TimeSeriesSummary.  # noqa: E501
        :type: DType
        """

        self._dtype = dtype

    @property
    def dparams(self):
        """Gets the dparams of this TimeSeriesSummary.  # noqa: E501

        parameters of data type, e.g. enum  # noqa: E501

        :return: The dparams of this TimeSeriesSummary.  # noqa: E501
        :rtype: object
        """
        return self._dparams

    @dparams.setter
    def dparams(self, dparams):
        """Sets the dparams of this TimeSeriesSummary.

        parameters of data type, e.g. enum  # noqa: E501

        :param dparams: The dparams of this TimeSeriesSummary.  # noqa: E501
        :type: object
        """

        self._dparams = dparams

    @property
    def itype(self):
        """Gets the itype of this TimeSeriesSummary.  # noqa: E501


        :return: The itype of this TimeSeriesSummary.  # noqa: E501
        :rtype: IType
        """
        return self._itype

    @itype.setter
    def itype(self, itype):
        """Sets the itype of this TimeSeriesSummary.


        :param itype: The itype of this TimeSeriesSummary.  # noqa: E501
        :type: IType
        """

        self._itype = itype

    @property
    def freq(self):
        """Gets the freq of this TimeSeriesSummary.  # noqa: E501


        :return: The freq of this TimeSeriesSummary.  # noqa: E501
        :rtype: Frequency
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this TimeSeriesSummary.


        :param freq: The freq of this TimeSeriesSummary.  # noqa: E501
        :type: Frequency
        """

        self._freq = freq

    @property
    def fparams(self):
        """Gets the fparams of this TimeSeriesSummary.  # noqa: E501

        parameters of time index type, e.g. time zone if applicable, pivot date, etc  # noqa: E501

        :return: The fparams of this TimeSeriesSummary.  # noqa: E501
        :rtype: object
        """
        return self._fparams

    @fparams.setter
    def fparams(self, fparams):
        """Sets the fparams of this TimeSeriesSummary.

        parameters of time index type, e.g. time zone if applicable, pivot date, etc  # noqa: E501

        :param fparams: The fparams of this TimeSeriesSummary.  # noqa: E501
        :type: object
        """

        self._fparams = fparams

    @property
    def entity(self):
        """Gets the entity of this TimeSeriesSummary.  # noqa: E501

        Entity is used in panel data to associate time series with a unit or individual, e.g. household or company, etc. It is used together with variable name to create a unique reference to time series in a panel collection, (entity, variable). Entity is immutable  # noqa: E501

        :return: The entity of this TimeSeriesSummary.  # noqa: E501
        :rtype: int
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this TimeSeriesSummary.

        Entity is used in panel data to associate time series with a unit or individual, e.g. household or company, etc. It is used together with variable name to create a unique reference to time series in a panel collection, (entity, variable). Entity is immutable  # noqa: E501

        :param entity: The entity of this TimeSeriesSummary.  # noqa: E501
        :type: int
        """

        self._entity = entity

    @property
    def variable(self):
        """Gets the variable of this TimeSeriesSummary.  # noqa: E501

        variable is used in panel data to associate time series with a cross-sectional measure, e.g. eye color, etc. It is used together with variable name to create a unique reference to time series in a panel collection, (entity, variable). Variable is immutable  # noqa: E501

        :return: The variable of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this TimeSeriesSummary.

        variable is used in panel data to associate time series with a cross-sectional measure, e.g. eye color, etc. It is used together with variable name to create a unique reference to time series in a panel collection, (entity, variable). Variable is immutable  # noqa: E501

        :param variable: The variable of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """
        if variable is not None and not re.search(r'^[a-zA-Z0-9]{6,60}$', variable):  # noqa: E501
            raise ValueError(r"Invalid value for `variable`, must be a follow pattern or equal to `/^[a-zA-Z0-9]{6,60}$/`")  # noqa: E501

        self._variable = variable

    @property
    def tsi(self):
        """Gets the tsi of this TimeSeriesSummary.  # noqa: E501

        Time Series Identifier as a string where ts name, collection name and space name as separated by comma  # noqa: E501

        :return: The tsi of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._tsi

    @tsi.setter
    def tsi(self, tsi):
        """Sets the tsi of this TimeSeriesSummary.

        Time Series Identifier as a string where ts name, collection name and space name as separated by comma  # noqa: E501

        :param tsi: The tsi of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """
        if tsi is not None and len(tsi) < 1:
            raise ValueError("Invalid value for `tsi`, length must be greater than or equal to `1`")  # noqa: E501
        if tsi is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{0,59}.[a-zA-Z][_a-zA-Z0-9]{4,60}.[a-zA-Z][_a-zA-Z0-9]{4,60}$', tsi):  # noqa: E501
            raise ValueError(r"Invalid value for `tsi`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{0,59}.[a-zA-Z][_a-zA-Z0-9]{4,60}.[a-zA-Z][_a-zA-Z0-9]{4,60}$/`")  # noqa: E501

        self._tsi = tsi

    @property
    def space(self):
        """Gets the space of this TimeSeriesSummary.  # noqa: E501


        :return: The space of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this TimeSeriesSummary.


        :param space: The space of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """
        if space is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{4,59}$', space):  # noqa: E501
            raise ValueError(r"Invalid value for `space`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{4,59}$/`")  # noqa: E501

        self._space = space

    @property
    def collection(self):
        """Gets the collection of this TimeSeriesSummary.  # noqa: E501


        :return: The collection of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this TimeSeriesSummary.


        :param collection: The collection of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """
        if collection is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{4,59}$', collection):  # noqa: E501
            raise ValueError(r"Invalid value for `collection`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{4,59}$/`")  # noqa: E501

        self._collection = collection

    @property
    def name(self):
        """Gets the name of this TimeSeriesSummary.  # noqa: E501

        unique series name in a collection  # noqa: E501

        :return: The name of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimeSeriesSummary.

        unique series name in a collection  # noqa: E501

        :param name: The name of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """
        if name is not None and not re.search(r'^[a-zA-Z][_a-zA-Z0-9]{0,59}$', name):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[a-zA-Z][_a-zA-Z0-9]{0,59}$/`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this TimeSeriesSummary.  # noqa: E501

        Title of time series  # noqa: E501

        :return: The title of this TimeSeriesSummary.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TimeSeriesSummary.

        Title of time series  # noqa: E501

        :param title: The title of this TimeSeriesSummary.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def discontinued(self):
        """Gets the discontinued of this TimeSeriesSummary.  # noqa: E501

        Time series, which are no longer recorded can be marked as discontinued. Discontinued series can be kept in the database for historical reasons  # noqa: E501

        :return: The discontinued of this TimeSeriesSummary.  # noqa: E501
        :rtype: bool
        """
        return self._discontinued

    @discontinued.setter
    def discontinued(self, discontinued):
        """Sets the discontinued of this TimeSeriesSummary.

        Time series, which are no longer recorded can be marked as discontinued. Discontinued series can be kept in the database for historical reasons  # noqa: E501

        :param discontinued: The discontinued of this TimeSeriesSummary.  # noqa: E501
        :type: bool
        """

        self._discontinued = discontinued

    @property
    def unit(self):
        """Gets the unit of this TimeSeriesSummary.  # noqa: E501

        units of values  # noqa: E501

        :return: The unit of this TimeSeriesSummary.  # noqa: E501
        :rtype: object
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TimeSeriesSummary.

        units of values  # noqa: E501

        :param unit: The unit of this TimeSeriesSummary.  # noqa: E501
        :type: object
        """

        self._unit = unit

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
        if not isinstance(other, TimeSeriesSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other