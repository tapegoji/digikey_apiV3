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


class KeywordSearchResponse(object):
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
        'limited_taxonomy': 'LimitedTaxonomy',
        'filter_options': 'list[LimitedParameter]',
        'products': 'list[Product]',
        'products_count': 'int',
        'exact_manufacturer_products_count': 'int',
        'exact_manufacturer_products': 'list[Product]',
        'exact_digi_key_product': 'Product',
        'search_locale_used': 'IsoSearchLocale'
    }

    attribute_map = {
        'limited_taxonomy': 'LimitedTaxonomy',
        'filter_options': 'FilterOptions',
        'products': 'Products',
        'products_count': 'ProductsCount',
        'exact_manufacturer_products_count': 'ExactManufacturerProductsCount',
        'exact_manufacturer_products': 'ExactManufacturerProducts',
        'exact_digi_key_product': 'ExactDigiKeyProduct',
        'search_locale_used': 'SearchLocaleUsed'
    }

    def __init__(self, limited_taxonomy=None, filter_options=None, products=None, products_count=None, exact_manufacturer_products_count=None, exact_manufacturer_products=None, exact_digi_key_product=None, search_locale_used=None, _configuration=None):  # noqa: E501
        """KeywordSearchResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._limited_taxonomy = None
        self._filter_options = None
        self._products = None
        self._products_count = None
        self._exact_manufacturer_products_count = None
        self._exact_manufacturer_products = None
        self._exact_digi_key_product = None
        self._search_locale_used = None
        self.discriminator = None

        if limited_taxonomy is not None:
            self.limited_taxonomy = limited_taxonomy
        if filter_options is not None:
            self.filter_options = filter_options
        if products is not None:
            self.products = products
        if products_count is not None:
            self.products_count = products_count
        if exact_manufacturer_products_count is not None:
            self.exact_manufacturer_products_count = exact_manufacturer_products_count
        if exact_manufacturer_products is not None:
            self.exact_manufacturer_products = exact_manufacturer_products
        if exact_digi_key_product is not None:
            self.exact_digi_key_product = exact_digi_key_product
        if search_locale_used is not None:
            self.search_locale_used = search_locale_used

    @property
    def limited_taxonomy(self):
        """Gets the limited_taxonomy of this KeywordSearchResponse.  # noqa: E501


        :return: The limited_taxonomy of this KeywordSearchResponse.  # noqa: E501
        :rtype: LimitedTaxonomy
        """
        return self._limited_taxonomy

    @limited_taxonomy.setter
    def limited_taxonomy(self, limited_taxonomy):
        """Sets the limited_taxonomy of this KeywordSearchResponse.


        :param limited_taxonomy: The limited_taxonomy of this KeywordSearchResponse.  # noqa: E501
        :type: LimitedTaxonomy
        """

        self._limited_taxonomy = limited_taxonomy

    @property
    def filter_options(self):
        """Gets the filter_options of this KeywordSearchResponse.  # noqa: E501

        Available filters for narrowing down results.  # noqa: E501

        :return: The filter_options of this KeywordSearchResponse.  # noqa: E501
        :rtype: list[LimitedParameter]
        """
        return self._filter_options

    @filter_options.setter
    def filter_options(self, filter_options):
        """Sets the filter_options of this KeywordSearchResponse.

        Available filters for narrowing down results.  # noqa: E501

        :param filter_options: The filter_options of this KeywordSearchResponse.  # noqa: E501
        :type: list[LimitedParameter]
        """

        self._filter_options = filter_options

    @property
    def products(self):
        """Gets the products of this KeywordSearchResponse.  # noqa: E501

        List of products returned by KeywordSearch  # noqa: E501

        :return: The products of this KeywordSearchResponse.  # noqa: E501
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this KeywordSearchResponse.

        List of products returned by KeywordSearch  # noqa: E501

        :param products: The products of this KeywordSearchResponse.  # noqa: E501
        :type: list[Product]
        """

        self._products = products

    @property
    def products_count(self):
        """Gets the products_count of this KeywordSearchResponse.  # noqa: E501

        Total number of matching products found.  # noqa: E501

        :return: The products_count of this KeywordSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._products_count

    @products_count.setter
    def products_count(self, products_count):
        """Sets the products_count of this KeywordSearchResponse.

        Total number of matching products found.  # noqa: E501

        :param products_count: The products_count of this KeywordSearchResponse.  # noqa: E501
        :type: int
        """

        self._products_count = products_count

    @property
    def exact_manufacturer_products_count(self):
        """Gets the exact_manufacturer_products_count of this KeywordSearchResponse.  # noqa: E501

        Number of exact ManufacturerPartNumber matches.  # noqa: E501

        :return: The exact_manufacturer_products_count of this KeywordSearchResponse.  # noqa: E501
        :rtype: int
        """
        return self._exact_manufacturer_products_count

    @exact_manufacturer_products_count.setter
    def exact_manufacturer_products_count(self, exact_manufacturer_products_count):
        """Sets the exact_manufacturer_products_count of this KeywordSearchResponse.

        Number of exact ManufacturerPartNumber matches.  # noqa: E501

        :param exact_manufacturer_products_count: The exact_manufacturer_products_count of this KeywordSearchResponse.  # noqa: E501
        :type: int
        """

        self._exact_manufacturer_products_count = exact_manufacturer_products_count

    @property
    def exact_manufacturer_products(self):
        """Gets the exact_manufacturer_products of this KeywordSearchResponse.  # noqa: E501

        List of products that are exact ManufacturerPartNumber matches.  # noqa: E501

        :return: The exact_manufacturer_products of this KeywordSearchResponse.  # noqa: E501
        :rtype: list[Product]
        """
        return self._exact_manufacturer_products

    @exact_manufacturer_products.setter
    def exact_manufacturer_products(self, exact_manufacturer_products):
        """Sets the exact_manufacturer_products of this KeywordSearchResponse.

        List of products that are exact ManufacturerPartNumber matches.  # noqa: E501

        :param exact_manufacturer_products: The exact_manufacturer_products of this KeywordSearchResponse.  # noqa: E501
        :type: list[Product]
        """

        self._exact_manufacturer_products = exact_manufacturer_products

    @property
    def exact_digi_key_product(self):
        """Gets the exact_digi_key_product of this KeywordSearchResponse.  # noqa: E501


        :return: The exact_digi_key_product of this KeywordSearchResponse.  # noqa: E501
        :rtype: Product
        """
        return self._exact_digi_key_product

    @exact_digi_key_product.setter
    def exact_digi_key_product(self, exact_digi_key_product):
        """Sets the exact_digi_key_product of this KeywordSearchResponse.


        :param exact_digi_key_product: The exact_digi_key_product of this KeywordSearchResponse.  # noqa: E501
        :type: Product
        """

        self._exact_digi_key_product = exact_digi_key_product

    @property
    def search_locale_used(self):
        """Gets the search_locale_used of this KeywordSearchResponse.  # noqa: E501


        :return: The search_locale_used of this KeywordSearchResponse.  # noqa: E501
        :rtype: IsoSearchLocale
        """
        return self._search_locale_used

    @search_locale_used.setter
    def search_locale_used(self, search_locale_used):
        """Sets the search_locale_used of this KeywordSearchResponse.


        :param search_locale_used: The search_locale_used of this KeywordSearchResponse.  # noqa: E501
        :type: IsoSearchLocale
        """

        self._search_locale_used = search_locale_used

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
        if issubclass(KeywordSearchResponse, dict):
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
        if not isinstance(other, KeywordSearchResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KeywordSearchResponse):
            return True

        return self.to_dict() != other.to_dict()
