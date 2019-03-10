API
===

.. note::
    Unless otherwise noted all arguments are of the :class:`str` type.

API Object
----------

.. automodule:: circleci.api
    :members:
    :private-members:

Experimental API Object
-----------------------

.. automodule:: circleci.experimental
    :members:


Errors
------

.. automodule:: circleci.error

.. autoclass:: circleci.error.CircleCIException
    :members:

.. autoclass:: circleci.error.BadVerbError
    :members:

    .. autoattribute:: message

.. autoclass:: circleci.error.BadKeyError
    :members:

    .. autoattribute:: message

.. autoclass:: circleci.error.InvalidFilterError
    :members:

    .. autoattribute:: filter_message
    .. autoattribute:: artifacts_message
