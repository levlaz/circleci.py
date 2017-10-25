# -*- coding: utf-8 -*-
"""
CircleCI API Error Module

:copyright: (c) 2017 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
class CircleCIError(Exception):
    """Base class for CircleCI errors"""
    pass


class BadHttpVerbError(CircleCIError):
    """Exception raises for bad HTTP verb

    Args:
        verb (str):
            HTTP Verb that was tried
        message (str):
            explanation message
    """
    def __init__(self, verb, message):
        self.verb = verb
        self.message = message


class BadKeyTypeError(CircleCIError):
    """Exception raises for bad Key Type

    Args:
        key_type (str):
            Value passed in for key_type
        message (str):
            explanation message
    """
    def __init__(self, key_type, message):
        self.key_type = key_type
        self.message = message