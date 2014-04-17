__author__ = 'kevin'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Plugin(object):
    name = ""
    description = ""

    def install(self):
        if self.is_install():
            print " * %s : can't install this plugin, it's already installed" % (self.name,)
        else:
            return self._install()
        return False

    def is_install(self):
        return self._is_install()

    def status(self):
        return self._status()

    def enable(self):
        if not self.is_install():
            print " * %s : can't enable this plugin, it's not installed" % (self.name,)
        else:
            if self.status():
                print " * %s : can't enable this plugin, already enabled" % (self.name,)
            else:
                if self._enable():
                    print " * %s : OK, this plugin is enable" % (self.name,)
                    return True
                else:
                    print " * %s : ERROR, this plugin cannot be enabled, sorry" % (self.name,)
        return False

    def disable(self):
        if not self.is_install():
            print " * %s : can't disable this plugin, it's not installed" % (self.name,)
        else:
            if not self.status():
                print " * %s : can't disable this plugin, already disabled" % (self.name,)
            else:
                if self._disable():
                    print " * %s : OK, this plugin is disabled" % (self.name,)
                    return True
                else:
                    print " * %s : ERROR, this plugin cannot be disabled, sorry" % (self.name,)
        return False

    def show_status(self):
        if not self.is_install():
            print bcolors.OKBLUE + " * %s : is not installed" % (self.name,) + bcolors.ENDC
        else:
            if self.status():
                print bcolors.OKGREEN + " * %s : is enabled" % (self.name,) + bcolors.ENDC
            else:
                print bcolors.WARNING + " * %s : is disabled" % (self.name,) + bcolors.ENDC

    def _is_install(self):
        return True

    def _install(self):
        return False

    def _disable(self):
        return False

    def _enable(self):
        return False

    def _status(self):
        return False