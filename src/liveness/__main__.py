#!/usr/bin/env python3
#
# MIT License
#
# (C) Copyright 2020-2022, 2024 Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
"""
This entrypoint is used to determine if this service is still active/alive
from a Kubernetes liveness probe perspective.

This service is deemed to be 'alive' and healthy if the
main loop has executed relatively recently. The period of time for how frequently
the agent checks for operational work is defined as a function of event frequency from
kubernetes, so this liveness probe needs a larger than normal window to account for
periods of time without a recent liveness cycle.

This main routine exists as an example; each project should implement their own
__main__ routine within their own liveness project. Then, a helm chart deployment may
reference the projects newly created module by adding:

      livenessProbe:
        exec:
         command:
         - python3
         - "-m"
         - "myservice.liveness"
        initialDelaySeconds: 10
        periodSeconds: 30

to the associated helmchart.

Created on April 30, 2020

@author: jsl
"""

import sys
import logging
import os

from liveness import TIMESTAMP_PATH
from liveness.timestamp import Timestamp


LOGGER = logging.getLogger('liveness.main')
DEFAULT_LOG_LEVEL = logging.INFO


def setup_logging():
    """
    Configure logger
    """
    log_format = "%(asctime)-15s - %(levelname)-7s - %(name)s - %(message)s"
    requested_log_level = os.environ.get('LOG_LEVEL', DEFAULT_LOG_LEVEL)
    log_level = logging.getLevelName(requested_log_level)
    logging.basicConfig(level=log_level, format=log_format)


if __name__ == '__main__':
    setup_logging()
    timestamp = Timestamp.byref(TIMESTAMP_PATH)
    if timestamp.alive:
        LOGGER.info("%s is considered valid; the application is alive!", timestamp)
        sys.exit(0)
    else:
        LOGGER.warning("Timestamp is no longer considered valid.")
        sys.exit(1)
