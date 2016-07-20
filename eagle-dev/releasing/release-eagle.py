#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Utility for creating well-formed pull request merges and pushing them to Apache.
#   usage: ./apache-pr-merge.py    (see config env vars below)
#
# This utility assumes you already have local a Eagle git folder and that you
# have added remotes corresponding to both (i) the github apache Eagle
# mirror and (ii) the apache git repo.

import logging
import sys

try:
    import jira.client
except ImportError:
    # TODO - Michael Wu: P1 - deal with jira client
    print "error occurs importing jira.client"

# TODO - Michael Wu: P2 - read log level from config
logger = logging.Logger(logging.LOG_LEVEL_NAME_DEBUG)

def main(arvs):
    logger.info("aaaa")

if __name__ == "__main__":
    main(sys.argv[1:])


