# -*- coding: utf-8 -*-
"""
:copyright: (c) 2017 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
import requests

from requests.auth import HTTPBasicAuth

from circleci.error import BadHttpVerbError

class Api():
    """A python interface into the CircleCI API"""

    def __init__(self, token, url='https://circleci.com/api/v1.1'):
        """Instantiate a new circleci.Api object.

        Args:
            url (str):
                The URL to the CircleCI instance
                defaults to https://circleci.com/api/v1.1

                If you are running CircleCI server, the API
                is available at the same endpoint of your own
                installation url. i.e (https://circleci.yourcompany.com/api/v1.1)

            token (str):
                Your CircleCI token.abs
        """
        self.token = token
        self.url = url

    def get_user_info(self):
        """Provides information about the signed in user."""
        resp = self._request('GET', 'me')
        return resp

    def get_projects(self):
        """List of all the projects you're following on CircleCI."""
        resp = self._request('GET', 'projects')
        return resp

    def follow_project(self, username, project, vcs_type='github'):
        """Follow a new project on CircleCI.

        Args:
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket
            username (str):
                github org or user name
            project (str):
                case sensitive repo name
        """
        endpoint = 'project/{0}/{1}/{2}/follow'.format(
            vcs_type,
            username,
            project
        )
        resp = self._request('POST', endpoint)
        return resp

    def _request(self, verb, endpoint):
        """Request a url.

        Args:
            endpoint (str):
                The api endpoint we want to call
            verb (str):
                POST or GET

        Returns:
            A JSON object with the response from the API
        """

        headers = {
            'Accept': 'application/json',
        }
        auth = HTTPBasicAuth(self.token, '')
        resp = None

        request_url = "{0}/{1}".format(self.url, endpoint)

        if verb == 'GET':
            resp = requests.get(request_url, auth=auth, headers=headers)

        elif verb == 'POST':
            resp = requests.post(request_url, auth=auth, headers=headers)

        else:
            raise BadHttpVerbError(verb, "verb must be GET or POST")

        return resp.json()
