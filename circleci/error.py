# -*- coding: utf-8 -*-
"""
CircleCI API Error Module

:copyright: (c) 2017 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
class CircleCIException(Exception):
    """Base class for CircleCI exceptions

    Args:
        argument: The argument that was passed into the function.
        message: explanation message.
    """
    def __init__(self, argument):
        super().__init__()
        self.argument = argument
        self.message = None

    def __str__(self):
        return '{0} is invalid. {1}'.format(self.argument, self.message)


class BadVerbError(CircleCIException):
    """Exception raises for bad HTTP verb"""
    def __init__(self, argument):
        super().__init__(argument)
        self.message = "verb must be one of 'GET', 'POST', or 'DELETE'"


class BadKeyError(CircleCIException):
    """Exception raises for bad Key Type"""
    def __init__(self, argument):
        super().__init__(argument)
        self.message = "key must be one of 'deploy-key' or 'github-user-key'"


class InvalidFilterError(CircleCIException):
    """Exception raises for an invalid filter"""
    def __init__(self, argument):
        super().__init__(argument)
        self.message = "status_filter must be one of 'completed'" \
            "'successful', 'failed', or 'running'"
