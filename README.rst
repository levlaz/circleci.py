circleci.py
===========

Python Wrapper around the CircleCI API

.. image:: https://circleci.com/gh/levlaz/circleci.py.svg?style=shield
    :target: https://circleci.com/gh/levlaz/circleci.py

.. image:: https://badge.fury.io/py/circleci.svg
    :target: https://badge.fury.io/py/circleci

Installation
============

::

    pip install circleci

Usage
=====

Make a `new API token <https://circleci.com/account/api>`__ in the CircleCI application.

Import the CircleCI API and start using methods

::

    from circleci.api import Api

    circleci = Api($YOUR_TOKEN)

    circleci.get_user_info()


See `the tests <https://github.com/levlaz/circleci.py/blob/master/tests/circle/test_api.py>`__ for more examples.

Limitations
===========

1. Build paramaters not yet supported
2. `These endpoints <https://github.com/levlaz/circleci.py/blob/master/circleci/api.py#L277>`__ are not yet supported.

Development
===========
Your life will be a lot better if you use a virtualenv when working with python.

1. Fork and Clone this repo
2. Install `python-pip <https://pip.pypa.io/en/stable/installing/>`__ and `virtualenv <https://virtualenv.pypa.io/en/stable/>`__ if you do not already have it.
3. Create a new virtualenv with ``virtualenv -p python3 env``.
4. Actiavte the new virtualenv with ``source env/bin/activate``.
5. Run ``make dev``
6. Hack away!
