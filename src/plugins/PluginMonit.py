__author__ = 'kevin'

from src.model.Plugin import Plugin
from src.model.Common import Common


class PluginMonit(Plugin):
    def __init__(self):
        self.name = "Monit"
        self.description = "Monitoring program (preconfigured for system,apache,mysql)"

    def _is_install(self):
        return Common.exist("/etc/monit/monitrc")

    def _install(self):
        # Execute install monit
        Common.execute("apt-get install monit")

        # Write system monitoring
        file = open("/etc/monit/conf.d/system", "w")
        file.write("check system local\n")
        file.write("    if loadavg (1min) > 4 then alert\n")
        file.write("    if loadavg (5min) > 2 then alert\n")
        file.write("    if memory usage > 80% then alert\n")
        file.write("    if cpu usage (user) > 80% then alert\n")
        file.write("    if cpu usage (system) > 50% then alert\n")
        file.write("    if cpu usage (wait) > 25% then alert\n")
        file.close()

        # Write apache monitoring
        file = open("/etc/monit/conf.d/apache2", "w")
        file.write("check process apache with pidfile /var/run/apache2.pid\n")
        file.write("    start program = \"/etc/init.d/apache2 start\"\n")
        file.write("    stop program = \"/etc/init.d/apache2 stop\"\n")
        file.write("    if failed host 127.0.0.1 port 80 protocol http\n")
        file.write("       and request \"/monit/token\" then restart\n")
        file.write("    if cpu is greater than 90% for 2 cycles then alert\n")
        file.write("    if cpu > 80%  for 5 cycles then restart\n")
        file.write("    if children > 250 then restart\n")
        file.write("    if loadavg(5min) greater than 10 for 8 cycles then stop\n")
        file.write("    if 3 restarts within 5 cycles then timeout\n")
        file.close()

        file = open("/etc/monit/conf.d/mysql", "w")
        file.write("check process mysql with pidfile /var/run/mysqld/mysqld.pid group database\n")
        file.write("    start program = \"/etc/init.d/mysql start\"\n")
        file.write("    stop program = \"/etc/init.d/mysql stop\"\n")
        file.write("    if failed unix \"/var/run/mysqld/mysqld.sock\" then restart\n")
        file.write("    if failed host 127.0.0.1 port 3306 then restart\n")
        file.write("    if 5 restarts within 5 cycles then timeout\n")
        file.close()

        # Execute monit restart
        Common.execute("/etc/init.d/monit reload")
        return True

    def _enable(self):
        Common.execute("/etc/init.d/monit start")
        return True

    def _disable(self):
        Common.execute("/etc/init.d/monit stop")
        return True

    def _status(self):
        data = Common.execute("/etc/init.d/monit status")
        if "monit is running" in data:
            return True
        return False