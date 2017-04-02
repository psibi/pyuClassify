#!/usr/bin/python
# Copyright (C) 2012 Sibi <sibi@psibi.in>
#
# This file is part of pyuClassify.
#
# pyuClassify program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyuClassify program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyuClassify program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyuClassify.  If not, see <http://www.gnu.org/licenses/>.
#
# Author:   Sibi <sibi@psibi.in>
from .uclassify_endpoints import uclassify_http_status_codes

class uClassifyError(Exception):
    """
       Generic error class, catches all the uClassify issues.
    """
    def __init__(self,msg,error_code=None):
        self.msg = msg
        self.error_code = error_code

        if error_code is not None and error_code in uclassify_http_status_codes:
            self.msg = '%s: %s --%s' % (uclassify_http_status_codes[error_code][0],uclassify_http_status_codes[error_code][1],self.msg)

    def __str__(self):
        return repr(self.msg)

