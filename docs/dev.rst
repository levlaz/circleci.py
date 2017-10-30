Developer Documentation
=======================

Installing Development Environment
----------------------------------

Your life will be a lot better if you use a virtualenv when working with python.

1. Fork and Clone this repo
2. Install `python-pip <https://pip.pypa.io/en/stable/installing/>`__ and `virtualenv <https://virtualenv.pypa.io/en/stable/>`__ if you do not already have it.
3. Create a new virtualenv with ``virtualenv -p python3 env``.
4. Actiavte the new virtualenv with ``source env/bin/activate``.
5. Run ``make dev``
6. Hack away!

Running Tests
-------------

Tests can be found in the ``tests`` directory. 

You can run tests with ``make tests``. 

If you want to run a specific test file you can do so with:

::

    python -m unittest tests/circle/test_$MODULE.py

This project has two main types of tests.

* Unit tests. These are tests of specific functions using mocked API data.
* Integration tests. These are tests that actually hit the CircleCI API. Unfortunately, due to the way that permissions work most of the currently written tests will only work properly for the ``levlaz`` user and token. 

Code Coverage
~~~~~~~~~~~~~

This project attempts to have 100% code coverage. when you run ``make test`` code coverage is automatically ran. You can view the code coverage report locally by opening up the index.html file in the ``htmlcov`` directory that gets created when you run ``make test``. 

Documentation
-------------

This project uses sphinx for documentation. You can generate the latest docs locally by running ``make docs``. You can then view them by opening up the ``index.html`` file in the ``docs/build/html`` directory. 

Linting and Style
-----------------

This project follows the `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guidelines. You can install ``pylint`` in order to ensure that all of your code is compliant with this standard. 



