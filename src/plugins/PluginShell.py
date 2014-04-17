__author__ = 'kevin'

from src.model.Plugin import Plugin
from src.model.Common import Common


class PluginShell(Plugin):
    def __init__(self):
        self.name = "Shell in a box"
        self.description = "The webshell than allow you to use ssh commands in a webpage"

    def _enable(self):
        Common.execute("/etc/init.d/shellinabox start", "Starting Daemon")
        Common.execute('sed -i "s|SHELLINABOX_DAEMON_START=0|SHELLINABOX_DAEMON_START=1|" /etc/default/shellinabox', "Add autostart config")
        return True

    def _disable(self):
        Common.execute("/etc/init.d/shellinabox stop", "Stopping Daemon")
        Common.execute('sed -i "s|SHELLINABOX_DAEMON_START=1|SHELLINABOX_DAEMON_START=0|" /etc/default/shellinabox', "Remove autostart config")
        return True

    def _status(self):
        response = Common.execute("cat /etc/default/shellinabox | grep DAEMON_START")
        if "=1" in response:
            return True
        return False