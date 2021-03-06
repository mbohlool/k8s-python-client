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


class V1ResourceQuotaSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1ResourceQuotaSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'hard': 'object',
            'scopes': 'list[V1ResourceQuotaScope]'
        }

        self.attribute_map = {
            'hard': 'hard',
            'scopes': 'scopes'
        }

        self._hard = None
        self._scopes = None

    @property
    def hard(self):
        """
        Gets the hard of this V1ResourceQuotaSpec.
        Hard is the set of desired hard limits for each named resource. More info: http://releases.k8s.io/HEAD/docs/design/admission_control_resource_quota.md#admissioncontrol-plugin-resourcequota

        :return: The hard of this V1ResourceQuotaSpec.
        :rtype: object
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """
        Sets the hard of this V1ResourceQuotaSpec.
        Hard is the set of desired hard limits for each named resource. More info: http://releases.k8s.io/HEAD/docs/design/admission_control_resource_quota.md#admissioncontrol-plugin-resourcequota

        :param hard: The hard of this V1ResourceQuotaSpec.
        :type: object
        """
        self._hard = hard

    @property
    def scopes(self):
        """
        Gets the scopes of this V1ResourceQuotaSpec.
        A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.

        :return: The scopes of this V1ResourceQuotaSpec.
        :rtype: list[V1ResourceQuotaScope]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this V1ResourceQuotaSpec.
        A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects.

        :param scopes: The scopes of this V1ResourceQuotaSpec.
        :type: list[V1ResourceQuotaScope]
        """
        self._scopes = scopes

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

