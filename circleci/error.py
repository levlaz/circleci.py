# -*- coding: utf-8 -*-
"""
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