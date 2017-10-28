circleci.py
===========

Python Wrapper around the CircleCI API

.. image:: https://circleci.com/gh/levlaz/circleci.py.svg?style=shield
    :target: https://circleci.com/gh/levlaz/circleci.py

.. image:: https://codecov.io/gh/levlaz/circleci.py/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/levlaz/circleci.py

.. image:: https://badge.fury.io/py/circleci.svg
    :target: https://badge.fury.io/py/circleci

.. image:: https://readthedocs.org/projects/circlecipy/badge/?version=latest
    :target: http://circlecipy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Installation
============

circleci.py requires Python 3. `Python 2 will be EOL <https://www.python.org/dev/peps/pep-0373/>`__ soon, it's time to make the switch.

::

    pip install circleci

Usage
=====

Basic Usage
-----------
Make a `new API token <https://circleci.com/account/api>`__ in the CircleCI application.

Import the CircleCI API and start using methods:

::

    from circleci.api import Api

    circleci = Api("$YOUR_TOKEN")

    circleci.get_user_info()

Usage with CircleCI server
--------------------------
Make a new API token at ``https://<$YOUR_CIRCLECI_DOMAIN>/account/api``.

Import the CircleCI API and start using methods:

::

    from circleci.api import Api

    circleci = Api("$YOUR_TOKEN", "$YOUR_CIRCLECI_DOMAIN/api/v1.1")

    circleci.get_user_info()

See `the tests <https://github.com/levlaz/circleci.py/blob/master/tests/circle/test_api.py>`__ for more examples.

Features
========

1. Supports the `latest v1.1 of the CircleCI API <https://circleci.com/docs/api/v1-reference/>`__.
2. Supports both circleci.com and `CircleCI server <https://circleci.com/enterprise/>`__ (aka "Enterprise").

Experimental Features
---------------------

**WARNING:**
All methods here work against the **UNDOCUMENTED** and **UNSUPPORTED** CircleCI
API. Subject to change at any moment. Use at your own risk.

* Retry a build without cache

::

    from circleci.experimental import Experimental

    circleci = Experimental("$YOUR_TOKEN")
    circleci.retry_no_cache('$USERNAME', '$PROJECT', '$BUILD_NUMBER')

Sample Output (truncated for readability)

::

    'author_date': '2017-10-24T12:00:27-07:00',
    'author_email': 'lev@circleci.com',
    'author_name': 'Lev Lazinskiy',
    'body': '',
    'branch': 'master',
    'build_num': 21,
    'fail_reason': None,
    'failed': None,
    'infrastructure_fail': False,
    'is_first_green_build': False,
    'job_name': None,
    'lifecycle': 'scheduled',
    'messages': [],

    ...

    'no_dependency_cache': True,

    ...


Development
===========
Your life will be a lot better if you use a virtualenv when working with python.

1. Fork and Clone this repo
2. Install `python-pip <https://pip.pypa.io/en/stable/installing/>`__ and `virtualenv <https://virtualenv.pypa.io/en/stable/>`__ if you do not already have it.
3. Create a new virtualenv with ``virtualenv -p python3 env``.
4. Actiavte the new virtualenv with ``source env/bin/activate``.
5. Run ``make dev``
6. Hack away!

Running Tests
-------------

Tests are stored in the ``tests/`` directory. You can run tests with ``make test``.
In order to run the integration tests you must have a valid ``CIRCLE_TOKEN`` set as an environment variable.