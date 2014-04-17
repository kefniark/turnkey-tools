__author__ = 'kevin'

from src.model.Plugin import Plugin
from src.model.Common import Common


class PluginPhpMyAdmin(Plugin):
    def __init__(self):
        self.name = "PhpMyAdmin"
        self.description = "The Phpmyadmin interface installed with turnkey"

    def _enable(self):
        Common.execute("a2ensite phpmyadmin", "Enable site phpmyadmin")
        Common.execute('service apache2 reload', "Restart Apache")
        return True

    def _disable(self):
        Common.execute("a2dissite phpmyadmin", "Disable site phpmyadmin")
        Common.execute('service apache2 reload', "Restart Apache")
        return True

    def _status(self):
        return Common.exist("/etc/apache2/sites-enabled/phpmyadmin")
