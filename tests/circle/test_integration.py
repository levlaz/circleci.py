# pylint: disable-all
import unittest
import json
import pprint
import os

from unittest.mock import MagicMock, patch
from circleci.api import Api
from circleci.error import BadHttpVerbError

class TestCircleCIApi(unittest.TestCase):

    def setUp(self):
        self.c = Api(os.getenv('CIRCLE_TOKEN'))

    def test_trigger_with_build_params(self):
        params = {
            "param1": "value1",
            "param2": "value2",
            "build_parameters[CIRCLE_JOB]": "test"
        }

        resp = self.c.trigger_build('levlaz', 'circleci-demo-javascript-express', params=params)

        self.assertEqual(resp['build_parameters']['CIRCLE_JOB'], 'test')