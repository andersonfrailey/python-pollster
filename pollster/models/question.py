# coding: utf-8

from pprint import pformat
from six import iteritems
import re


class Question(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, slug=None, name=None, tags=None, charts=None, election_date=None, n_polls=None, created_at=None, responses=None):
        """
        Question - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'slug': 'str',
            'name': 'str',
            'tags': 'list[str]',
            'charts': 'list[str]',
            'election_date': 'date',
            'n_polls': 'int',
            'created_at': 'datetime',
            'responses': 'list[QuestionResponses]'
        }

        self.attribute_map = {
            'slug': 'slug',
            'name': 'name',
            'tags': 'tags',
            'charts': 'charts',
            'election_date': 'election_date',
            'n_polls': 'n_polls',
            'created_at': 'created_at',
            'responses': 'responses'
        }

        self._slug = slug
        self._name = name
        self._tags = tags
        self._charts = charts
        self._election_date = election_date
        self._n_polls = n_polls
        self._created_at = created_at
        self._responses = responses


    @property
    def slug(self):
        """
        Gets the slug of this Question.
        Unique Question identifier. For example: `obama-job-approval`. May contain spaces, symbols and capital letters.

        :return: The slug of this Question.
        :rtype: str
        """
        return self._slug

    @property
    def name(self):
        """
        Gets the name of this Question.
        Gist of the question, phrased such that a journalist on the beat will understand what it represents. For example: `2016 West Virginia Governor: Cole vs. Justice`

        :return: The name of this Question.
        :rtype: str
        """
        return self._name

    @property
    def tags(self):
        """
        Gets the tags of this Question.
        All Tag slugs for Tags on this Question

        :return: The tags of this Question.
        :rtype: list[str]
        """
        return self._tags

    @property
    def charts(self):
        """
        Gets the charts of this Question.
        All Chart slugs for Charts built from this Question

        :return: The charts of this Question.
        :rtype: list[str]
        """
        return self._charts

    @property
    def election_date(self):
        """
        Gets the election_date of this Question.
        Date of the election pertaining to this Question, or `null` if the question does not pertain to an upcoming election

        :return: The election_date of this Question.
        :rtype: date
        """
        return self._election_date

    @property
    def n_polls(self):
        """
        Gets the n_polls of this Question.
        Number of Poll objects that ask this Question. Use the `polls` API endpoint with the `question` parameter for Poll details

        :return: The n_polls of this Question.
        :rtype: int
        """
        return self._n_polls

    @property
    def created_at(self):
        """
        Gets the created_at of this Question.
        Date Pollster editors first created this Question

        :return: The created_at of this Question.
        :rtype: datetime
        """
        return self._created_at

    @property
    def responses(self):
        """
        Gets the responses of this Question.
        Responses Pollster editors decided upon. Individual polls have their own responses which often differ from these responses.

        :return: The responses of this Question.
        :rtype: list[QuestionResponses]
        """
        return self._responses

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