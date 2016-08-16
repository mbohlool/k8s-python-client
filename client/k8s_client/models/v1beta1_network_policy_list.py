# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class V1beta1NetworkPolicyList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1beta1NetworkPolicyList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'items': 'list[V1beta1NetworkPolicy]',
            'kind': 'str',
            'metadata': 'UnversionedListMeta'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'items': 'items',
            'kind': 'kind',
            'metadata': 'metadata'
        }

        self._api_version = None
        self._items = None
        self._kind = None
        self._metadata = None

    @property
    def api_version(self):
        """
        Gets the api_version of this V1beta1NetworkPolicyList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1beta1NetworkPolicyList.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1beta1NetworkPolicyList.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1beta1NetworkPolicyList.
        :type: str
        """
        self._api_version = api_version

    @property
    def items(self):
        """
        Gets the items of this V1beta1NetworkPolicyList.
        Items is a list of schema objects.

        :return: The items of this V1beta1NetworkPolicyList.
        :rtype: list[V1beta1NetworkPolicy]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this V1beta1NetworkPolicyList.
        Items is a list of schema objects.

        :param items: The items of this V1beta1NetworkPolicyList.
        :type: list[V1beta1NetworkPolicy]
        """
        self._items = items

    @property
    def kind(self):
        """
        Gets the kind of this V1beta1NetworkPolicyList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1beta1NetworkPolicyList.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1beta1NetworkPolicyList.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1beta1NetworkPolicyList.
        :type: str
        """
        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1beta1NetworkPolicyList.


        :return: The metadata of this V1beta1NetworkPolicyList.
        :rtype: UnversionedListMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1beta1NetworkPolicyList.


        :param metadata: The metadata of this V1beta1NetworkPolicyList.
        :type: UnversionedListMeta
        """
        self._metadata = metadata

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

