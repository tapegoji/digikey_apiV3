# coding: utf-8

"""
    PartSearch Api

    Search for products and retrieve details and pricing.  # noqa: E501

    OpenAPI spec version: Ps2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class ParametricFilter(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'parameter_id': 'int',
        'value_id': 'str'
    }

    attribute_map = {
        'parameter_id': 'ParameterId',
        'value_id': 'ValueId'
    }

    def __init__(self, parameter_id=None, value_id=None, _configuration=None):  # noqa: E501
        """ParametricFilter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parameter_id = None
        self._value_id = None
        self.discriminator = None

        if parameter_id is not None:
            self.parameter_id = parameter_id
        if value_id is not None:
            self.value_id = value_id

    @property
    def parameter_id(self):
        """Gets the parameter_id of this ParametricFilter.  # noqa: E501

        The parameter identifier.  # noqa: E501

        :return: The parameter_id of this ParametricFilter.  # noqa: E501
        :rtype: int
        """
        return self._parameter_id

    @parameter_id.setter
    def parameter_id(self, parameter_id):
        """Sets the parameter_id of this ParametricFilter.

        The parameter identifier.  # noqa: E501

        :param parameter_id: The parameter_id of this ParametricFilter.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                parameter_id is not None and parameter_id > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `parameter_id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self._configuration.client_side_validation and
                parameter_id is not None and parameter_id < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `parameter_id`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._parameter_id = parameter_id

    @property
    def value_id(self):
        """Gets the value_id of this ParametricFilter.  # noqa: E501

        The value identifier.  # noqa: E501

        :return: The value_id of this ParametricFilter.  # noqa: E501
        :rtype: str
        """
        return self._value_id

    @value_id.setter
    def value_id(self, value_id):
        """Sets the value_id of this ParametricFilter.

        The value identifier.  # noqa: E501

        :param value_id: The value_id of this ParametricFilter.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                value_id is not None and len(value_id) > 100):
            raise ValueError("Invalid value for `value_id`, length must be less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                value_id is not None and len(value_id) < 1):
            raise ValueError("Invalid value for `value_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._value_id = value_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ParametricFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParametricFilter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ParametricFilter):
            return True

        return self.to_dict() != other.to_dict()
