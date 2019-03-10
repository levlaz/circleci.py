# -*- coding: utf-8 -*-
"""
CircleCI SDK Module

.. versionadded:: 1.2.0

:copyright: (c) 2019 by Lev Lazinskiy
:license: MIT, see LICENSE for more details.
"""
import time
import os

from circleci.api import Api

class SDK():
    """CircleCI SDK

    An SDK module that allows you to do interesting or complex things using
    the CircleCI API.
    """

    def __init__(self, apiclient: Api, logger=None):
        """Instantiate a new circleci.SDK object.

        :param apiclient: an instance of circleci.Api
        """
        self.apiclient = apiclient
        self.logger = logger

    def _log(self, msg: str):
        """Log helper

        Emits logs if a logger is provided. Otherwise uses ``print()``.

        :param msg: log message
        """
        if self.logger is not None:
            self.logger.info(msg)
        else:
            print(msg)

    def _get_running_builds(self, username: str, project: str, vcs_type: str) -> list:
        """Get up to 100 running builds for a single project.

        :param username: Org or user name.
        :param project: Case sensitive repo name.
        :param vcs_type: Defaults to github. On circleci.com you can \
            also pass in ``bitbucket``.

        :returns: an array of build URLs.
        """
        _PROJECT_BUILD_LIMIT = 100
        _BUILD_STATUS = 'running'

        running_builds = self.apiclient.get_project_build_summary(
            username = username,
            project = project,
            limit = _PROJECT_BUILD_LIMIT,
            status_filter = _BUILD_STATUS,
            vcs_type = vcs_type
        )

        return [build['build_url'] for build in running_builds]


    def build_singleton(self, username, project, vcs_type='github'):
        """
        Force builds for a specific project to run one at a time.

        This method gets a build summary for a specific project to see
        all currently running builds. It filters out the current running
        build. It pauses execution until the project has no more running
        builds.

        It will recheck for running builds every 15 seconds.

        :param username: Org or user name.
        :param project: Case sensitive repo name.
        :param vcs_type: Defaults to github. On circleci.com you can \
            also pass in ``bitbucket``.

        .. versionchanged:: 1.2.2
            fixed bug where current build was counted toward running builds.
        """
        _SLEEP_INTERVAL_SECONDS = 15

        def _get_other_builds():
            """
            Get running builds except for this one.

            CIRCLE_BUILD_URL is set by default in all CircleCI builds.
            """
            error_msg = ("CIRCLE_BUILD_URL was not found. You may be "
                "running this script outside of a CircleCI build.")

            rb = self._get_running_builds(username, project, vcs_type)
            try:
                rb.remove(os.environ.get('CIRCLE_BUILD_URL'))
            except ValueError:
                self._log(error_msg)
            if len(rb) > 0:
                self._log(rb)
            return rb

        while len(_get_other_builds()) > 0:
            self._log('found running builds, sleeping for {0} seconds. \
                '.format(_SLEEP_INTERVAL_SECONDS))
            time.sleep(_SLEEP_INTERVAL_SECONDS)

        self._log('no running builds found, beginning execution.')
