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


class V1beta1TokenReviewStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        V1beta1TokenReviewStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'authenticated': 'bool',
            'error': 'str',
            'user': 'V1beta1UserInfo'
        }

        self.attribute_map = {
            'authenticated': 'authenticated',
            'error': 'error',
            'user': 'user'
        }

        self._authenticated = None
        self._error = None
        self._user = None

    @property
    def authenticated(self):
        """
        Gets the authenticated of this V1beta1TokenReviewStatus.
        Authenticated indicates that the token was associated with a known user.

        :return: The authenticated of this V1beta1TokenReviewStatus.
        :rtype: bool
        """
        return self._authenticated

    @authenticated.setter
    def authenticated(self, authenticated):
        """
        Sets the authenticated of this V1beta1TokenReviewStatus.
        Authenticated indicates that the token was associated with a known user.

        :param authenticated: The authenticated of this V1beta1TokenReviewStatus.
        :type: bool
        """
        self._authenticated = authenticated

    @property
    def error(self):
        """
        Gets the error of this V1beta1TokenReviewStatus.
        Error indicates that the token couldn't be checked

        :return: The error of this V1beta1TokenReviewStatus.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this V1beta1TokenReviewStatus.
        Error indicates that the token couldn't be checked

        :param error: The error of this V1beta1TokenReviewStatus.
        :type: str
        """
        self._error = error

    @property
    def user(self):
        """
        Gets the user of this V1beta1TokenReviewStatus.


        :return: The user of this V1beta1TokenReviewStatus.
        :rtype: V1beta1UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1beta1TokenReviewStatus.


        :param user: The user of this V1beta1TokenReviewStatus.
        :type: V1beta1UserInfo
        """
        self._user = user

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

