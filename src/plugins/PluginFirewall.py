__author__ = 'kevin'

from src.model.Plugin import Plugin
from src.model.Common import Common


class PluginFirewall(Plugin):
    def __init__(self):
        self.name = "Firewall"
        self.description = "Turnkey's firewall"

    def _enable(self):
        return False

    def _disable(self):
        return False

    def _status(self):
        return Common.check_url("https://127.0.0.1:12321")
