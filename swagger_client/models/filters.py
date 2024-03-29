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


class Filters(object):
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
        'taxonomy_ids': 'list[int]',
        'manufacturer_ids': 'list[int]',
        'parametric_filters': 'list[ParametricFilter]'
    }

    attribute_map = {
        'taxonomy_ids': 'TaxonomyIds',
        'manufacturer_ids': 'ManufacturerIds',
        'parametric_filters': 'ParametricFilters'
    }

    def __init__(self, taxonomy_ids=None, manufacturer_ids=None, parametric_filters=None, _configuration=None):  # noqa: E501
        """Filters - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._taxonomy_ids = None
        self._manufacturer_ids = None
        self._parametric_filters = None
        self.discriminator = None

        if taxonomy_ids is not None:
            self.taxonomy_ids = taxonomy_ids
        if manufacturer_ids is not None:
            self.manufacturer_ids = manufacturer_ids
        if parametric_filters is not None:
            self.parametric_filters = parametric_filters

    @property
    def taxonomy_ids(self):
        """Gets the taxonomy_ids of this Filters.  # noqa: E501

        A collection of Taxonomy Ids to filter on. Ids can be found in the initial search response. A a full list ids can be found from the Search Categories endpoint  # noqa: E501

        :return: The taxonomy_ids of this Filters.  # noqa: E501
        :rtype: list[int]
        """
        return self._taxonomy_ids

    @taxonomy_ids.setter
    def taxonomy_ids(self, taxonomy_ids):
        """Sets the taxonomy_ids of this Filters.

        A collection of Taxonomy Ids to filter on. Ids can be found in the initial search response. A a full list ids can be found from the Search Categories endpoint  # noqa: E501

        :param taxonomy_ids: The taxonomy_ids of this Filters.  # noqa: E501
        :type: list[int]
        """

        self._taxonomy_ids = taxonomy_ids

    @property
    def manufacturer_ids(self):
        """Gets the manufacturer_ids of this Filters.  # noqa: E501

        A collection of Manufacturer Ids to filter on. Ids can be found in the initial search response. A a full list ids can be found from the Search Manufactures endpoint  # noqa: E501

        :return: The manufacturer_ids of this Filters.  # noqa: E501
        :rtype: list[int]
        """
        return self._manufacturer_ids

    @manufacturer_ids.setter
    def manufacturer_ids(self, manufacturer_ids):
        """Sets the manufacturer_ids of this Filters.

        A collection of Manufacturer Ids to filter on. Ids can be found in the initial search response. A a full list ids can be found from the Search Manufactures endpoint  # noqa: E501

        :param manufacturer_ids: The manufacturer_ids of this Filters.  # noqa: E501
        :type: list[int]
        """

        self._manufacturer_ids = manufacturer_ids

    @property
    def parametric_filters(self):
        """Gets the parametric_filters of this Filters.  # noqa: E501

        A collection of ParametricFilters. A ParametricFilter consists of a ParameterId and a ValueId. Those Ids can also be found in the Search response.  # noqa: E501

        :return: The parametric_filters of this Filters.  # noqa: E501
        :rtype: list[ParametricFilter]
        """
        return self._parametric_filters

    @parametric_filters.setter
    def parametric_filters(self, parametric_filters):
        """Sets the parametric_filters of this Filters.

        A collection of ParametricFilters. A ParametricFilter consists of a ParameterId and a ValueId. Those Ids can also be found in the Search response.  # noqa: E501

        :param parametric_filters: The parametric_filters of this Filters.  # noqa: E501
        :type: list[ParametricFilter]
        """

        self._parametric_filters = parametric_filters

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
        if issubclass(Filters, dict):
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
        if not isinstance(other, Filters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Filters):
            return True

        return self.to_dict() != other.to_dict()
