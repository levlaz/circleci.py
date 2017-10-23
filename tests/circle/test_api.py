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
            token = os.getenv('CIRCLE_CI_TOKEN'),
            url='https://ccie-preview.sphereci.com/api/v1.1')

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

    def test_follow_project(self):
        self.loadMock('mock_follow_project_response')
        resp = json.loads(self.c.follow_project('ccie-tester', 'testing'))

        self.assertEqual(resp["mock+following"], True)

    def test_get_project_build_summary(self):
        self.loadMock('mock_project_build_summary_response')
        resp = json.loads(self.c.get_project_build_summary('ccie-tester', 'testing'))

        self.assertEqual(len(resp), 6)
        self.assertEqual(resp[0]['username'], 'MOCK+ccie-tester')

    def test_get_recent_builds(self):
        self.loadMock('mock_get_recent_builds_response')
        resp = json.loads(self.c.get_recent_builds())

        self.assertEqual(len(resp), 7)
        self.assertEqual(resp[0]['reponame'], 'MOCK+testing')

    def test_get_build_info(self):
        self.loadMock('mock_get_build_info_response')
        resp = json.loads(self.c.get_build_info('ccie-tester', 'testing', '1'))

        self.assertEqual(resp['reponame'], 'MOCK+testing')

    def test_get_artifacts(self):
        self.loadMock('mock_get_artifacts_response')
        resp = json.loads(self.c.get_artifacts('ccie-tester', 'testing', '1'))

        self.assertEqual(resp[0]['path'], 'MOCK+raw-test-output/go-test-report.xml')

    def test_retry_build(self):
        self.loadMock('mock_retry_build_response')
        resp = json.loads(self.c.retry_build('ccie-tester', 'testing', '1'))

        self.assertEqual(resp['reponame'], 'MOCK+testing')

    def test_cancel_build(self):
        self.loadMock('mock_cancel_build_response')
        resp = json.loads(self.c.cancel_build('ccie-tester', 'testing', '11'))

        self.assertEqual(resp['reponame'], 'MOCK+testing')
        self.assertEqual(resp['build_num'], 11)
        self.assertTrue(resp['canceled'])

    def test_add_ssh_user(self):
        self.loadMock('mock_add_ssh_user_response')
        resp = json.loads(self.c.add_ssh_user('ccie-tester', 'testing', '11'))

        self.assertEqual(resp['reponame'], 'MOCK+testing')
        self.assertEqual(resp['ssh_users'][0]['login'], 'ccie-tester')

    # def test_add_ssh_key(self):
    #     resp = self.c.create_ssh_key('ccie-tester', 'testing')
    #     with open('tests/mocks/mock_create_ssh_key_response', 'w') as f:
    #          json.dump(resp, f)

    #     print(resp)

    def test_trigger_build(self):
        self.loadMock('mock_trigger_build_response')
        resp = json.loads(self.c.trigger_build('ccie-tester', 'testing'))

        self.assertEqual(resp['reponame'], 'MOCK+testing')