#!/usr/bin/python

from uclassify_endpoints import uclassify_http_status_codes

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

