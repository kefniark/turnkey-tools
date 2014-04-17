#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Your application """


class Application:
    def __init__(self):
        self.plugins = {}
        self.init_plugins()

    def enable_debug(self):
        from model.Common import Common
        Common.set_debug(True)

    def init_plugins(self):
        from src.plugins.PluginWebmin import PluginWebmin
        from src.plugins.PluginShell import PluginShell
        from src.plugins.PluginPhpMyAdmin import PluginPhpMyAdmin
        from src.plugins.PluginMonit import PluginMonit

        self.plugins['phpmyadmin'] = PluginPhpMyAdmin()
        self.plugins['shellinabox'] = PluginShell()
        self.plugins['webmin'] = PluginWebmin()
        self.plugins['monit'] = PluginMonit()

    def show_plugins(self):
        print "list of available plugins :"
        for plugin in self.plugins.items():
            print " * " + plugin[0] + " - " + plugin[1].description

    def status(self, plugin_name):
        if plugin_name in self.plugins.keys():
            print "Status of the %s plugin :" % (plugin_name,)
            plugin = self.plugins[plugin_name]
            plugin.show_status()
        elif plugin_name == "all":
            print "Status of all plugins :"
            for plugin in self.plugins.iteritems():
                plugin[1].show_status()
        else:
            print "Plugin %s is unknown" % (plugin_name,)
            return False

    def install(self, plugin_name):
        if plugin_name in self.plugins.keys():
            print "Enable the %s plugin :" % (plugin_name,)
            plugin = self.plugins[plugin_name]
            plugin.install()
        else:
            print "Plugin %s is unknown" % (plugin_name,)
            return False

    def enable(self, plugin_name):
        if plugin_name in self.plugins.keys():
            print "Enable the %s plugin :" % (plugin_name,)
            plugin = self.plugins[plugin_name]
            plugin.enable()
        elif plugin_name == "all":
            print "Enable all the plugins :"
            for plugin in self.plugins.iteritems():
                plugin[1].enable()
        else:
            print "Plugin %s is unknown" % (plugin_name,)
            return False

    def disable(self, plugin_name):
        if plugin_name in self.plugins.keys():
            print "Disable the %s plugin :" % (plugin_name,)
            plugin = self.plugins[plugin_name]
            plugin.disable()
        elif plugin_name == "all":
            print "Disable all the plugins :"
            for plugin in self.plugins.iteritems():
                plugin[1].disable()
        else:
            print "Plugin %s is unknown" % (plugin_name,)
            return False

    def main(self, options, args):
        if not args:
            args = ['all']
        if len(args) == 2:
            options.action = args[1]
        if options.action == "status":
            self.status(args[0])
        elif options.action == "install":
            self.install(args[0])
        elif options.action == "enable":
            self.enable(args[0])
        elif options.action == "disable":
            self.disable(args[0])
        else:
            print "Action %s is unknown" % (options.action,)
        #else:
        #    print "Hum ... You don't gave me anything to do :'("
        #    print "Use -h / --help if you wan't to see possibles parameters to feed me"

#just for development
if __name__ == "__main__":
    app = Application()
    app.show_plugins()
    #app.status("all")

    app.status("webmin")
    app.enable("webmin")
    app.status("webmin")
    app.disable("webmin")
    app.status("webmin")
