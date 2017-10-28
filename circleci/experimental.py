# -*- coding: utf-8 -*-
"""
CircleCI Experimental API Module

.. admonition:: Notice

    All methods here work against **undocumented** and **unsupported** aspects of the
    CircleCI API. Subject to change at any moment. Use at your own risk.

:copyright: (c) 2017 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
from circleci.api import Api

class Experimental(Api):
    """Experimantal CircleCI API"""

    def retry_no_cache(self, username, project, build_num, vcs_type='github'):
        """Retries a build without cache

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
        params = {
            "no-cache": "true",
        }

        endpoint = 'project/{0}/{1}/{2}/{3}/retry'.format(
            vcs_type,
            username,
            project,
            build_num
        )

        resp = self._request('POST', endpoint, params)
        return resp

