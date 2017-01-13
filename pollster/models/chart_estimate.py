# coding: utf-8

from pprint import pformat
from six import iteritems
import re


class ChartEstimate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, algorithm=None, created_at=None, datetime=None, values=None, lowess_parameters=None, bayesian_kallman_95_percent_intervals=None):
        """
        ChartEstimate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'algorithm': 'str',
            'created_at': 'datetime',
            'datetime': 'datetime',
            'values': 'object',
            'lowess_parameters': 'ChartEstimateLowessParameters',
            'bayesian_kallman_95_percent_intervals': 'object'
        }

        self.attribute_map = {
            'algorithm': 'algorithm',
            'created_at': 'created_at',
            'datetime': 'datetime',
            'values': 'values',
            'lowess_parameters': 'lowess_parameters',
            'bayesian_kallman_95_percent_intervals': 'bayesian_kallman_95_percent_intervals'
        }

        self._algorithm = algorithm
        self._created_at = created_at
        self._datetime = datetime
        self._values = values
        self._lowess_parameters = lowess_parameters
        self._bayesian_kallman_95_percent_intervals = bayesian_kallman_95_percent_intervals


    @property
    def algorithm(self):
        """
        Gets the algorithm of this ChartEstimate.
        Name of the algorithm that produced these estimates. Possible values are: `bayesian-kallman` ([source code](https://github.com/huffpostdata/pollster-models/tree/master/poll-average), [academic explanation](http://eppsac.utdallas.edu/files/jackman/CAJP%2040-4%20Jackman.pdf)); `lowess` (locally weighted scatterplot smoothing).

        :return: The algorithm of this ChartEstimate.
        :rtype: str
        """
        return self._algorithm

    @property
    def created_at(self):
        """
        Gets the created_at of this ChartEstimate.
        The time Pollster produced these estimates. Consider `datetime` instead. `datetime` describes what Pollster calculates; `created_at` describes _when_ Pollster made those calculations.

        :return: The created_at of this ChartEstimate.
        :rtype: datetime
        """
        return self._created_at

    @property
    def datetime(self):
        """
        Gets the datetime of this ChartEstimate.
        The time these `values` apply to. For instance, Pollster may run `lowess` (which is deterministic) years after an election; in that case `created_at` will be the date of the `lowess` calculation, and `datetime` will be the election date.

        :return: The datetime of this ChartEstimate.
        :rtype: datetime
        """
        return self._datetime

    @property
    def values(self):
        """
        Gets the values of this ChartEstimate.
        Each key is a response Label. Each value is Pollster's estimate of the polling average for that label. For instance, `{ \"Clinton\": 47.3, \"Trump\": 42.0, \"Other\": 5.2 }`. Values often do not add up to 100%. Some Responses on a Question have no corresponding Values, because Pollster sometimes omits Responses from a Chart. 

        :return: The values of this ChartEstimate.
        :rtype: object
        """
        return self._values

    @property
    def lowess_parameters(self):
        """
        Gets the lowess_parameters of this ChartEstimate.


        :return: The lowess_parameters of this ChartEstimate.
        :rtype: ChartEstimateLowessParameters
        """
        return self._lowess_parameters

    @property
    def bayesian_kallman_95_percent_intervals(self):
        """
        Gets the bayesian_kallman_95_percent_intervals of this ChartEstimate.
        Only present if `algorithm` is `bayesian-kallman`. Each key is a response Label. Each value is the `{ low, high }` of the algorithm's 95% confidence interval.

        :return: The bayesian_kallman_95_percent_intervals of this ChartEstimate.
        :rtype: object
        """
        return self._bayesian_kallman_95_percent_intervals

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