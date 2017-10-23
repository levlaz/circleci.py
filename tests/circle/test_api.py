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
        self.c = Api(
            token = os.getenv('CIRCLE_CI_TOKEN'))

    def loadMock(self, filename):
        """helper function to open mock responses"""
        filename = 'tests/mocks/{0}'.format(filename)

        with open(filename, 'r') as f:
            self.c._request = MagicMock(return_value=f.read())

    def test_bad_verb(self):

        with self.assertRaises(BadHttpVerbError) as e:
            self.c._request('BAD', 'dummy')

        self.assertEqual('BAD', e.exception.verb)
        self.assertIn('GET or POST', e.exception.message)

    def test_get_user_info(self):
        self.loadMock('mock_user_info_response')
        resp = json.loads(self.c.get_user_info())

        self.assertEqual(resp["selected_email"], 'mock+ccie-tester@circleci.com')

    def test_get_projects(self):
        self.loadMock('mock_get_projects_response')
        resp = json.loads(self.c.get_projects())

        self.assertEqual(resp[0]['vcs_url'], 'MOCK+https://ghe-dev.circleci.com/ccie-tester/testing')


