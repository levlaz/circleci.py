# pylint: disable-all
import unittest

from circleci.error import CircleCIException, BadKeyError, BadVerbError, InvalidFilterError


class TestCircleCIError(unittest.TestCase):

    def setUp(self):
        self.base = CircleCIException('fake')
        self.key = BadKeyError('fake')
        self.verb = BadVerbError('fake')
        self.filter = InvalidFilterError('fake', 'status')
        self.afilter = InvalidFilterError('fake', 'artifacts')

    def test_error_implements_str(self):
        self.assertTrue(self.base.__str__ is not object.__str__)
        string = self.base.__str__()
        self.assertIn('invalid', string)

    def test_verb_message(self):
        self.assertIn('DELETE', self.verb.message)

    def test_key_message(self):
        self.assertIn('deploy-key', self.key.message)

    def test_filter_message(self):
        self.assertIn('running', self.filter.message)
        self.assertIn('completed', self.afilter.message)
