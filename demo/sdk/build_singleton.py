# -*- coding: utf-8 -*-
"""
demo.sdk.build_singleton
~~~~~~~~~~~~~~~~~~~~~~~~

Demonstrate how to use the circleci.py SDK to make builds run
one at a time.

The purpose of this script is to be executed early in a CircleCI job. It will
check for running builds, if it finds any it will pause execution and poll at
a 15 second interval. Once other jobs have finished it will continue execution.
If no jobs are found, it will start execution.

.. literalinclude:: ../demo/sdk/build_singleton.py
    :language: python
    :linenos:
    :lines: 61-72

Usage
    * Make sure a valid ``CIRCLE_TOKEN`` is set as an environment variable.
    * Replace ``ORG`` and ``REPO`` with your own values.
    * ``ORG`` can be either a username or an org name.
    * If you are using bitbucket you should add the ``vcs_type``
      argument to ``build_singleton``.

        .. code-block:: python

            sdk.build_singleton(ORG, REPO, vcs_type='bitbucket')

Within a CircleCI job you can do something like this in order to execute this
script. Assuming you have this ``build_singleton.py`` script checked into a
directory called ``scripts`` in your code repository.

.. code-block:: yaml
    :linenos:

        - run:
            name: Build Singleton
            command: |
                sudo pip install circleci.py
                python scripts/build_singleton.py

If builds are running you will see the following output in CircleCI:

.. code-block:: bash

        found running builds, sleeping for 15 seconds.
        ['https://circleci.com/gh/levlaz/circleci-sandbox/1148', 'https://circleci.com/gh/levlaz/circleci-sandbox/1147', 'https://circleci.com/gh/levlaz/circleci-sandbox/1146']
        found running builds, sleeping for 15 seconds.
        ['https://circleci.com/gh/levlaz/circleci-sandbox/1146']
        found running builds, sleeping for 15 seconds.
        ['https://circleci.com/gh/levlaz/circleci-sandbox/1146']

Once no more jobs are found, the job will begin to execute and you will see the
following output in CircleCI:

.. code-block:: bash

        no running builds found, beginning execution.
"""
import os
from circleci.api import Api
from circleci.sdk import SDK

ORG = "levlaz"
REPO = "circleci-sandbox"

circleci = Api(os.environ.get("CIRCLE_TOKEN"))
sdk = SDK(circleci)

if __name__ == "__main__":
    sdk.build_singleton(ORG, REPO)
