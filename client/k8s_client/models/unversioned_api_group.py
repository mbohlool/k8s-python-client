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


class UnversionedAPIGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UnversionedAPIGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'kind': 'str',
            'name': 'str',
            'preferred_version': 'UnversionedGroupVersionForDiscovery',
            'server_address_by_client_cid_rs': 'list[UnversionedServerAddressByClientCIDR]',
            'versions': 'list[UnversionedGroupVersionForDiscovery]'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'kind': 'kind',
            'name': 'name',
            'preferred_version': 'preferredVersion',
            'server_address_by_client_cid_rs': 'serverAddressByClientCIDRs',
            'versions': 'versions'
        }

        self._api_version = None
        self._kind = None
        self._name = None
        self._preferred_version = None
        self._server_address_by_client_cid_rs = None
        self._versions = None

    @property
    def api_version(self):
        """
        Gets the api_version of this UnversionedAPIGroup.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this UnversionedAPIGroup.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this UnversionedAPIGroup.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this UnversionedAPIGroup.
        :type: str
        """
        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind of this UnversionedAPIGroup.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this UnversionedAPIGroup.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this UnversionedAPIGroup.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this UnversionedAPIGroup.
        :type: str
        """
        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this UnversionedAPIGroup.
        name is the name of the group.

        :return: The name of this UnversionedAPIGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnversionedAPIGroup.
        name is the name of the group.

        :param name: The name of this UnversionedAPIGroup.
        :type: str
        """
        self._name = name

    @property
    def preferred_version(self):
        """
        Gets the preferred_version of this UnversionedAPIGroup.


        :return: The preferred_version of this UnversionedAPIGroup.
        :rtype: UnversionedGroupVersionForDiscovery
        """
        return self._preferred_version

    @preferred_version.setter
    def preferred_version(self, preferred_version):
        """
        Sets the preferred_version of this UnversionedAPIGroup.


        :param preferred_version: The preferred_version of this UnversionedAPIGroup.
        :type: UnversionedGroupVersionForDiscovery
        """
        self._preferred_version = preferred_version

    @property
    def server_address_by_client_cid_rs(self):
        """
        Gets the server_address_by_client_cid_rs of this UnversionedAPIGroup.
        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.

        :return: The server_address_by_client_cid_rs of this UnversionedAPIGroup.
        :rtype: list[UnversionedServerAddressByClientCIDR]
        """
        return self._server_address_by_client_cid_rs

    @server_address_by_client_cid_rs.setter
    def server_address_by_client_cid_rs(self, server_address_by_client_cid_rs):
        """
        Sets the server_address_by_client_cid_rs of this UnversionedAPIGroup.
        a map of client CIDR to server address that is serving this group. This is to help clients reach servers in the most network-efficient way possible. Clients can use the appropriate server address as per the CIDR that they match. In case of multiple matches, clients should use the longest matching CIDR. The server returns only those CIDRs that it thinks that the client can match. For example: the master will return an internal IP CIDR only, if the client reaches the server using an internal IP. Server looks at X-Forwarded-For header or X-Real-Ip header or request.RemoteAddr (in that order) to get the client IP.

        :param server_address_by_client_cid_rs: The server_address_by_client_cid_rs of this UnversionedAPIGroup.
        :type: list[UnversionedServerAddressByClientCIDR]
        """
        self._server_address_by_client_cid_rs = server_address_by_client_cid_rs

    @property
    def versions(self):
        """
        Gets the versions of this UnversionedAPIGroup.
        versions are the versions supported in this group.

        :return: The versions of this UnversionedAPIGroup.
        :rtype: list[UnversionedGroupVersionForDiscovery]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """
        Sets the versions of this UnversionedAPIGroup.
        versions are the versions supported in this group.

        :param versions: The versions of this UnversionedAPIGroup.
        :type: list[UnversionedGroupVersionForDiscovery]
        """
        self._versions = versions

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

