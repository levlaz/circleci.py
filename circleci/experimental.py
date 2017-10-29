# -*- coding: utf-8 -*-
"""
CircleCI Experimental API Module

.. warning::

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

        :param username: Org or user name.
        :param project: Case sensitive repo name.
        :param build_num: Build number.
        :param vcs_type: Defaults to github. On circleci.com you can \
            also pass in ``bitbucket``.

        :type build_num: int

        Endpoint:
            POST: ``/project/:vcs-type/:username/:project/:build_num/retry``
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

