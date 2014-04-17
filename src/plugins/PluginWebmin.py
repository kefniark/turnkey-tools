__author__ = 'kevin'

from src.model.Plugin import Plugin
from src.model.Common import Common


class PluginWebmin(Plugin):
    def __init__(self):
        self.name = "Webmin"
        self.description = "The administration interface, to easily manage your server"

    def _enable(self):
        Common.execute("/etc/webmin/start")
        return True

    def _disable(self):
        Common.execute("/etc/webmin/stop")
        return True

    def _status(self):
        return Common.check_url("https://127.0.0.1:12321")
