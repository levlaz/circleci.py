# pylint: disable-all
import json
import os
import pprint
import unittest
from unittest.mock import MagicMock, patch

from circleci.api import Api
from circleci.experimental import Experimental
from circleci.error import BadKeyError, BadVerbError, InvalidFilterError


class TestCircleCIApi(unittest.TestCase):

    def setUp(self):
        self.c = Api(os.getenv('CIRCLE_TOKEN'))

    def test_trigger_with_build_params(self):
        params = {
            "build_parameters[CIRCLE_JOB]": "build"
        }

        resp = self.c.trigger_build('levlaz', 'circleci.py', params=params)

        self.assertEqual(resp['build_parameters']['CIRCLE_JOB'], 'build')

    def test_add_ssh_key(self):

        # note this is a throwaway key
        key = """
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAr74mGZIij/V59DTGRPaijyDolWA33FlyopBVSys09MOOF7HT
EWLMwyyRIR3t6mjl7kcS3rTPWORLF4U+8iMv1EyitV+fV+pQIJmK8gZvyyNePCR0
wvAizhNTcYgtZF86D/EBNHwOdN0o4P+4qlbBlPjFiW7S5X6iDbrV9H4ADQDI2R+c
EBets+aVRrtCdR+cGrOS9BRVf4NK6ADQaKOcgTYRTJuxI48O18iUj9dZSCAlO6xQ
obpALlQKj0srGcx9++vTzED3Wr9JpOfsC8LqNdJdaF6KJfBsc1xczSw980hcXwWx
/zrQaii5W7nFU2lRrwdXyscqutL1I5lLKDYhLQIDAQABAoIBACA9mxG/3HVajGf/
sov+Ty5A1EprH3ReOIiYP/2NTKbGpW+1YMpkvLnlmC5iJj6FxgDjqxOOSie9ogUL
ndOgHusssADkLQBc7Rw97t6dza6Pq38PFRiaI1h49Srz15f9XFKGXTk6tRA9bn1w
jHk7d0IULXEcErald6dbKlszLmE0AHvWHWNrABwbNBzG2PrFFbrWbYiUDhIx8Ebj
9IKDu8JqYr5o6Kv8agOAWkq4S3iGQ9S+suTiV+3/kyK7XL5TI5gVPdZR4NIAGFKO
+1TBNtCiYl+LQ46km5cmirESTsObNM3JrF8VWBlVZoVrxZiIhYUAKrFzcJ905Vrh
PN0rwmECgYEA6LWeorGs9kyVgNI4KnvVI1AXACnpy4L48ypqIns5A71j+4OiVI64
dWAlHB64ZoMVVBqTCv/uiloqzlK+FCe8cxi3Xh/hBDmKmGZygpFoRdGwmNA+1CoA
DZftaswUQ64Qt8jc9HmQnufvkxniNAewRxuZDP462WgBwZhRe8hvUqUCgYEAwVT0
HojCaLm2TMY2XE9EzCHNF1XlfqzB0i0dJ4pQ2SZ8st1F8vkEjHsPEOURRkLzWFC4
A/QWFsmhv4UKpDplV5QV3S+FgbpzLdV64vUYBuo06OZGcJgCdtZyt6vGSB4f+mq2
VQt+j6ZYlI5nWwkz1Yvg8AmBemuXNFui8o/c9ekCgYB2vwa9+nBKFnZLj/n9I8d1
B49VFA4rPSAP5VrXUY2cbO4yD8+r2lAiBPeqy7pJBSbDDfRurn5otu4U7n/0BPrS
uJAJRbcq0rn4Xn6cRdqxlfjJYapN1UjFpvsNfinxB0ecoLCvR8EWdT/5DkIxTqMT
BfApgylAeyQ6R6F8yqCTyQKBgQCN5XFrO8scnDmt7ckWRWPkQ2bJGtVe/SMgxNXi
IIWoa7QYf4mIhLaO+P8c0lO0cw0yI8R7ulnADet2qwodcXLSLbFCb0+Y4KUK3eXc
0DD7WkjNK75Fg3xDhrAaGKxmYB3uaQY8MzyH6HqZRk+bpIxzzr+gzglHNdJ7rkpR
p79wiQKBgQCwFyjcLAfA5uJDZ9jVEZ2BKgd9IGo16HrRnd+mpggUBGf2mbE2JGgk
rAUZ8tU0o5Ec6T0ZQkcous7OwBZGE+JLuFa3S6JfISLw42brjQ9dE5mosm7m2d4H
3C9cAnmV6aJkTwT46OiNvUYZ8je5WP+4Kqb2ke9xw3ddk5X1n5AB4w==
-----END RSA PRIVATE KEY-----
"""
        resp = self.c.add_ssh_key('levlaz', 'circleci-sandbox', key, hostname='localhost')

        # there is no response when success, so we test to make sure
        # that there is no other message as well.
        self.assertTrue(len(resp) == 0)

    def test_get_user_info(self):
        # exercise a real "GET"
        resp = self.c.get_user_info()

        self.assertEqual(resp['login'], 'levlaz')

    def test_clear_cache(self):
        # execrise a real "DELETE"
        resp = self.c.clear_cache('levlaz', 'circleci-sandbox')

        self.assertEqual(resp['status'], 'build dependency caches deleted')

    def test_retry_build_no_cache(self):
        # use Experimental API
        self.e = Experimental(os.getenv('CIRCLE_TOKEN'))

        resp = self.e.retry_no_cache('levlaz', 'circleci-sandbox', 1)

        self.assertTrue(resp['no_dependency_cache'])

    def test_add_heroku_key(self):
        key = os.getenv('HEROKU_KEY')

        resp = self.c.add_heroku_key(key)

        # there is no response when success, so we test to make sure
        # that there is no other message as well.
        self.assertTrue(len(resp) == 0)

    def test_download_artifact(self):
        resp = self.c.get_artifacts('levlaz', 'circleci.py', 87)

        artifact = self.c.download_artifact(resp[0]['url'])

        self.assertIn('circleci_api_py.html', artifact)

        artifact_with_destdir = self.c.download_artifact(resp[0]['url'], '/tmp')

        self.assertIn('tmp', artifact_with_destdir)

        artifact_with_destdir_and_filename = self.c.download_artifact(resp[0]['url'], '/tmp', 'myartifact.txt')

        self.assertIn('myartifact.txt', artifact_with_destdir_and_filename)