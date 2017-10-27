# pylint: disable-all
import json
import os
import pprint
import unittest
from unittest.mock import MagicMock

from circleci.api import Api
from circleci.error import BadKeyError, BadVerbError, InvalidFilterError


class TestCircleCIApi(unittest.TestCase):

    def setUp(self):
        self.c = Api(os.getenv('CIRCLE_TOKEN'))

    def loadMock(self, filename):
        """helper function to open mock responses"""
        filename = 'tests/mocks/{0}'.format(filename)

        with open(filename, 'r') as f:
            self.c._request = MagicMock(return_value=f.read())

    def test_bad_verb(self):

        with self.assertRaises(BadVerbError) as e:
            self.c._request('BAD', 'dummy')

        self.assertEqual('BAD', e.exception.argument)
        self.assertIn('DELETE', e.exception.message)

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

        # with invalid status filter
        with self.assertRaises(InvalidFilterError) as e:
            json.loads(self.c.get_project_build_summary('ccie-tester', 'testing', status_filter='dummy'))

        self.assertEqual('dummy', e.exception.argument)
        self.assertIn('running', e.exception.message)

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

    def test_trigger_build(self):
        self.loadMock('mock_trigger_build_response')
        resp = json.loads(self.c.trigger_build('ccie-tester', 'testing'))

        self.assertEqual(resp['reponame'], 'MOCK+testing')

    def test_list_checkout_keys(self):
        self.loadMock('mock_list_checkout_keys_response')
        resp = json.loads(self.c.list_checkout_keys('levlaz', 'circleci-sandbox'))

        self.assertEqual(resp[0]['type'], 'deploy-key')
        self.assertIn('public_key', resp[0])

    def test_create_checkout_key(self):

        with self.assertRaises(BadKeyError) as e:
            self.c.create_checkout_key('levlaz', 'test', 'bad')

        self.assertEqual('bad', e.exception.argument)
        self.assertIn('deploy-key', e.exception.message)

        self.loadMock('mock_create_checkout_key_response')
        resp = json.loads(self.c.create_checkout_key('levlaz', 'test', 'deploy-key'))

        self.assertEqual(resp['type'], 'deploy-key')
        self.assertIn('public_key', resp)

    def test_get_checkout_key(self):

        self.loadMock('mock_get_checkout_key_response')
        resp = json.loads(self.c.get_checkout_key('levlaz', 'circleci-sandbox', '94:19:ab:a9:f4:2b:21:1c:a5:87:dd:ee:3d:c2:90:4e'))

        self.assertEqual(resp['type'], 'deploy-key')
        self.assertIn('public_key', resp)

    def test_delete_checkout_key(self):
        self.loadMock('mock_delete_checkout_key_response')
        resp = json.loads(self.c.delete_checkout_key('levlaz', 'circleci-sandbox', '94:19:ab:a9:f4:2b:21:1c:a5:87:dd:ee:3d:c2:90:4e'))

        self.assertEqual(resp['message'], 'ok')

    def test_clear_cache(self):
        self.loadMock('mock_clear_cache_response')
        resp = json.loads(self.c.clear_cache('levlaz', 'circleci-sandbox'))

        self.assertEqual('build dependency caches deleted', resp['status'])

    # def test_helper(self):
    #     resp = self.c.add_circle_key()
    #     print(resp)
    #     with open('tests/mocks/mock_add_circle_key_response', 'w') as f:
    #          json.dump(resp, f)
