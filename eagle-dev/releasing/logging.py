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

import re
import constants

# for log level:
LOG_LEVEL_NAME_DEBUG = "debug"
LOG_LEVEL_VALUE_DEBUG = 0
LOG_LEVEL_NAME_INFO = "info"
LOG_LEVEL_VALUE_INFO = 1
LOG_LEVEL_NAME_WARN = "warn"
LOG_LEVEL_VALUE_WARN = 2
LOG_LEVEL_NAME_ERROR = "error"
LOG_LEVEL_VALUE_ERROR = 3
LOG_LEVEL_NAME_FATAL = "fatal"
LOG_LEVEL_VALUE_FATAL = 4
DEFAULT_LOG_LEVEL_NAME = LOG_LEVEL_NAME_INFO
LOG_LEVEL_REGEXP = re.compile("^(%s|%s|%s|%s|%s)$" % (
    LOG_LEVEL_NAME_DEBUG, LOG_LEVEL_NAME_INFO, LOG_LEVEL_NAME_WARN, LOG_LEVEL_NAME_ERROR, LOG_LEVEL_NAME_FATAL), re.I)
LOG_LEVEL_MAPPING = dict()
LOG_LEVEL_MAPPING[LOG_LEVEL_NAME_DEBUG] = LOG_LEVEL_VALUE_DEBUG
LOG_LEVEL_MAPPING[LOG_LEVEL_NAME_INFO] = LOG_LEVEL_VALUE_INFO
LOG_LEVEL_MAPPING[LOG_LEVEL_NAME_WARN] = LOG_LEVEL_VALUE_WARN
LOG_LEVEL_MAPPING[LOG_LEVEL_NAME_ERROR] = LOG_LEVEL_VALUE_ERROR
LOG_LEVEL_MAPPING[LOG_LEVEL_NAME_FATAL] = LOG_LEVEL_VALUE_FATAL

class Logger:
    def __init__(self, level=LOG_LEVEL_NAME_INFO):
        match = LOG_LEVEL_REGEXP.search(level)
        if match:
            matched_value = match.group(1).lower()
            self.level_num = LOG_LEVEL_MAPPING[matched_value]
        else:
            print ("un-recognized log level: %s" % level)
            raise AttributeError("un-recognized log level: %s" % level)

    def __shall_log__(self, level_number):
        return level_number >= self.level_num

    def __log_msg_list__(self, key, msg):
        if isinstance(msg, list):
            for sm in msg:
                self.__to_console__("%s: %s" % (key, sm))
        elif isinstance(msg, str):
            self.__to_console__("%s: %s" % (key, msg))
        elif isinstance(msg, unicode):
            self.__to_console__("%s: %s" % (key, msg.encode(constants.ENCODING)))
        else:
            raise AttributeError("argument 'msg' must be a string, unicode or list, but %s is given" % type(msg))

    def __to_console__(self, msg):
        print msg

    def fatal(self, msg):
        if self.__shall_log__(LOG_LEVEL_VALUE_FATAL):
            self.__log_msg_list__("FTL", msg)

    def error(self, msg):
        if self.__shall_log__(LOG_LEVEL_VALUE_ERROR):
            self.__log_msg_list__("ERR", msg)

    def warn(self, msg):
        if self.__shall_log__(LOG_LEVEL_VALUE_WARN):
            self.__log_msg_list__("WRN", msg)

    def info(self, msg):
        if self.__shall_log__(LOG_LEVEL_VALUE_INFO):
            self.__log_msg_list__("INF", msg)

    def debug(self, msg):
        if self.__shall_log__(self, LOG_LEVEL_VALUE_DEBUG):
            self.__log_msg_list__("DBG", msg)