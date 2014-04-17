#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Script to run your app via command line

Usage: app_cli.py param1 param2

Options:
-h --help                   Show this screen.
-v --version                Show the app version
"""
from __future__ import absolute_import
from optparse import OptionParser, OptionGroup
from src import app

def main():
    """Main entry point for script."""

    # Declarations of Option Parser : https://docs.python.org/2/library/optparse.html
    parser = OptionParser(version="1.0")
    parser.add_option("-l", "--list", help="the plugin list", action="store_true", dest="list", default=False)
    parser.add_option("-a", "--action", help="the action you want to execute", dest="action", default="status")
    parser.add_option("--verbose", help="show executed commands", action="store_true", dest="debug", default=False)
    (options, args) = parser.parse_args()

    # Show the plugin list
    if options.list:
        app.show_plugins()
        return True

    # Enable the debugging
    if options.debug:
        app.enable_debug()

    # Calling the main function
    app.main(options, args)


if __name__ == "__main__":
    main()
