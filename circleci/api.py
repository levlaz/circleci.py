# -*- coding: utf-8 -*-
"""
CircleCI API Module

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
        """Provides information about the signed in user.

        Endpoint:
            GET: /me
        """
        resp = self._request('GET', 'me')
        return resp

    def get_projects(self):
        """List of all the projects you're following on CircleCI.

        Endpoint:
            GET: /projects
        """
        resp = self._request('GET', 'projects')
        return resp

    def follow_project(self, username, project, vcs_type='github'):
        """Follow a new project on CircleCI.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket

        Endpoint:
            POST: /project/:vcs-type/:username/:project/follow
        """
        endpoint = 'project/{0}/{1}/{2}/follow'.format(
            vcs_type,
            username,
            project
        )
        resp = self._request('POST', endpoint)
        return resp

    def get_project_build_summary(self, username, project, vcs_type='github'):
        """Build summary for each of the last 30 builds for a single git repo.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket

        Endpoint:
            GET: /project/:vcs-type/:username/:project
        """
        endpoint = 'project/{0}/{1}/{2}'.format(
            vcs_type,
            username,
            project
        )
        resp = self._request('GET', endpoint)
        return resp

    def get_recent_builds(self):
        """
        Build summary for each of the last 30 recent builds, ordered by build_num.

        Endpoint:
            GET: /recent-builds
        """
        resp = self._request('GET', 'recent-builds')
        return resp

    def get_build_info(self, username, project, build_num, vcs_type='github'):
        """Full details for a single build.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            build_num (str):
                build number
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket

        Endpoint:
            GET: /project/:vcs-type/:username/:project/:build_num
        """
        endpoint = 'project/{0}/{1}/{2}/{3}'.format(
            vcs_type,
            username,
            project,
            build_num
        )
        resp = self._request('GET', endpoint)
        return resp

    def get_artifacts(self, username, project, build_num, vcs_type='github'):
        """List the artifacts produced by a given build.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            build_num (str):
                build number
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket

        Endpoint:
            GET: /project/:vcs-type/:username/:project/:build_num/artifacts
        """
        endpoint = 'project/{0}/{1}/{2}/{3}/artifacts'.format(
            vcs_type,
            username,
            project,
            build_num
        )
        resp = self._request('GET', endpoint)
        return resp

    def retry_build(self, username, project, build_num, vcs_type='github'):
        """Retries the build.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            build_num (str):
                build number
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket

        Endpoint:
            POST: /project/:vcs-type/:username/:project/:build_num/retry
        """
        endpoint = 'project/{0}/{1}/{2}/{3}/retry'.format(
            vcs_type,
            username,
            project,
            build_num
        )
        resp = self._request('POST', endpoint)
        return resp

    def cancel_build(self, username, project, build_num, vcs_type='github'):
        """Cancels the build.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            build_num (str):
                build number
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket

        Endpoint:
            POST: /project/:vcs-type/:username/:project/:build_num/cancel
        """
        endpoint = 'project/{0}/{1}/{2}/{3}/cancel'.format(
            vcs_type,
            username,
            project,
            build_num
        )
        resp = self._request('POST', endpoint)
        return resp

    def add_ssh_user(self, username, project, build_num, vcs_type='github'):
        """Adds a user to the build's SSH permissions.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            build_num (str):
                build number
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket

        Endpoint:
            POST: /project/:vcs-type/:username/:project/:build_num/ssh-users
        """
        endpoint = 'project/{0}/{1}/{2}/{3}/ssh-users'.format(
            vcs_type,
            username,
            project,
            build_num
        )
        resp = self._request('POST', endpoint)
        return resp


    def trigger_build(
            self,
            username,
            project,
            branch='master',
            vcs_type='github',
            params=None):
        """
        Triggers a new build.

        Args:
            username (str):
                org or user name
            project (str):
                case sensitive repo name
            branch (str):
                defaults to master
            vcs_type (str):
                defaults to github
                on circleci.com you can also pass in bitbucket
            params (dict):
                optional build parameters
                https://circleci.com/docs/1.0/parameterized-builds/

        Endpoint:
            POST: /project/:vcs-type/:username/:project/tree/:branch
        """
        endpoint = 'project/{0}/{1}/{2}/tree/{3}'.format(
            vcs_type,
            username,
            project,
            branch
        )

        resp = self._request('POST', endpoint, params)
        return resp


# TODO support the rest of these methods
# POST: /project/:vcs-type/:username/:project/ssh-key
#     Create an ssh key used to access external systems that require SSH key-based authentication
# GET: /project/:vcs-type/:username/:project/checkout-key
#     Lists checkout keys.
# POST: /project/:vcs-type/:username/:project/checkout-key
#     Create a new checkout key.
# GET: /project/:vcs-type/:username/:project/checkout-key/:fingerprint
#     Get a checkout key.
# DELETE: /project/:vcs-type/:username/:project/checkout-key/:fingerprint
#     Delete a checkout key.
# DELETE: /project/:vcs-type/:username/:project/build-cache
#     Clears the cache for a project.
# POST: /user/ssh-key
#     Adds a CircleCI key to your GitHub User account.
# POST: /user/heroku-key
#     Adds your Heroku API key to CircleCI, takes apikey as form param name.


    def _request(self, verb, endpoint, data=None):
        """Request a url.

        Args:
            endpoint (str):
                The api endpoint we want to call
            verb (str):
                POST or GET
            params (dict):
                optional build parameters

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
            resp = requests.post(request_url, auth=auth, headers=headers, data=data)

        else:
            raise BadHttpVerbError(verb, "verb must be GET or POST")

        return resp.json()
