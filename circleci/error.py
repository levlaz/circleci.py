# -*- coding: utf-8 -*-
"""
circleci.error
~~~~~~~~~~~~~~

    This module provides some classes that subclass Exception to provide
    some useful exceptions for the API wrapper.
"""


class CircleCIException(Exception):
    """Base class for CircleCI exceptions

    :param argument: The argument that was passed into the function.
    """
    def __init__(self, argument):
        super().__init__()
        self.argument = argument
        self.message = None

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)


class BadVerbError(CircleCIException):
    """Exception raises for bad HTTP verb

    :param argument: The argument that was passed into the function.
    """
    message = "verb must be one of 'GET', 'POST', or 'DELETE'"

    def __init__(self, argument):
        super().__init__(argument)
        self.message = BadVerbError.message


class BadKeyError(CircleCIException):
    """Exception raises for bad Key Type

    :param argument: The argument that was passed into the function.
    """
    message = "key must be one of 'deploy-key' or 'github-user-key'"

    def __init__(self, argument):
        super().__init__(argument)
        self.message = BadKeyError.message


class InvalidFilterError(CircleCIException):
    """Exception raises for an invalid filter

    :param argument: The argument that was passed into the function.
    :param filter_type: Filter for status or artifacts.
    """
    filter_message = "status_filter must be one of 'completed'" \
        "'successful', 'failed', or 'running'"
    artifacts_message = "must be one of 'completed', 'successful', or 'failed'"

    def __init__(self, argument, filter_type):
        super().__init__(argument)
        if filter_type == 'status':
            self.message = InvalidFilterError.filter_message
        if filter_type == 'artifacts':
            self.message = InvalidFilterError.artifacts_message
