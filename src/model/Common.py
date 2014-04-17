__author__ = 'kevin'

import traceback
import commands
import os

class Common:
    debug = False

    @staticmethod
    def set_debug(value):
        Common.debug = value

    @staticmethod
    def log(message):
        if Common.debug:
            print " > %s" % (message,)

    @staticmethod
    def check_url(url):
        import urllib2

        try:
            Common.log("check url %s exist" % (url,))
            response = urllib2.urlopen(url)
            return response.read()
        except:
            pass
        return False

    @staticmethod
    def execute(cmd, info=None):
        if info:
            Common.log("%s : %s" % (info, cmd,))
        else:
            Common.log("%s" % (cmd,))
        return commands.getoutput(cmd)

    @staticmethod
    def exist(file_path):
        Common.log("check file %s exist" % (file_path,))
        return os.path.exists(file_path)