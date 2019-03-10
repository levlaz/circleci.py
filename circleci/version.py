"""
circleci.version
~~~~~~~~~~~~~~~~~~~~~~~

Helper file to set version in various places.

.. versionadded:: 1.2.0
"""
VERSION = "1.2.2"
"""Current version of circleci.py."""

def get_short_version() -> str:
    """
    Format "short" version in the form of X.Y

    :returns: short version
    """
    ver = VERSION.split(".")
    short_version = "{0}.{1}".format(ver[0], ver[1])
    return short_version
