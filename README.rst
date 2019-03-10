circleci.py
===========

Python Wrapper and SDK around the CircleCI API

.. image:: https://circleci.com/gh/levlaz/circleci.py.svg?style=shield
    :target: https://circleci.com/gh/levlaz/circleci.py
    :alt: CI Status

.. image:: https://codecov.io/gh/levlaz/circleci.py/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/levlaz/circleci.py
    :alt: Code Coverage

.. image:: https://badge.fury.io/py/circleci.svg
    :target: https://badge.fury.io/py/circleci
    :alt: PyPi PAckage

.. image:: https://readthedocs.org/projects/circlecipy/badge/?version=latest
    :target: http://circlecipy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Warnings
========

* circleci.py does not yet fully support CircleCI 2.1 or the Workflows API

Features
========

1. Supports the `latest v1.1 of the CircleCI API <https://circleci.com/docs/api/v1-reference/>`__.
2. Supports both circleci.com and `CircleCI server <https://circleci.com/enterprise/>`__ (aka "Enterprise").
3. Experimental API endpoints using undocumented aspects of the API.

Installation
============

circleci.py requires Python 3. `Python 2 will be EOL <https://www.python.org/dev/peps/pep-0373/>`__ soon, it's time to make the switch.

::

    pip install circleci

Quickstart
==========

Make a `new API token <https://circleci.com/account/api>`__ in the CircleCI application.

Import the CircleCI API and start using methods:

::

    from circleci.api import Api

    circleci = Api("$YOUR_TOKEN")

    # get info about your user
    circleci.get_user_info()

    # get list of all of your projects
    circleci.get_projects()

* You can read the `general documentation <https://circlecipy.readthedocs.io/en/latest/?badge=latest>`_ for more information about using circleci.py.
* If you are interesting in hacking on this library, check out the `developer documentation <https://circlecipy.readthedocs.io/en/latest/dev.html>`_.

Real World Examples
===================

Here are a couple of real world examples of this library being used. If you want to add your example here, open up a PR.

* `Lambda Function to Deploy via CircleCI <https://github.com/launchdarkly/SupportService/blob/master/LdLambda.py>`_ -- in this example the library is used to trigger deployment jobs in response to a webhook that triggers an AWS Lambda Job via AWS API Gateway.

Contributing
============

Please create an issue with a description of your problem, or open a pull request with a fix.

License
=======

MIT

Original Author
===============

Lev Lazinskiy - `https://levlaz.org <https://levlaz.org>`_
