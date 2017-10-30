Quickstart
==========

Installation
-------------

.. note::
    circleci.py requires python3

You can install the latest version of circleci.py with: 

::

    pip install circleci

Basic Usage
-----------

Make a `new API token <https://circleci.com/account/api>`__ in the CircleCI application.

Import the CircleCI API and start using methods:

::

    from circleci.api import Api

    circleci = Api("$YOUR_TOKEN")

    # get info about your user 
    circleci.get_user_info()

    # get list of all of your projects
    circleci.get_projects()

