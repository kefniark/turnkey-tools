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
    group = OptionGroup(parser, "Specific Options", "Your application parameters")
    group.add_option("-v", "--view", help="Show this software version", action="store_true", dest="view", default=False)
    group.add_option("-n", "--name", dest="name", help="Set a name")
    parser.add_option_group(group)
    (options, args) = parser.parse_args()

    # You're actions
    if options.view:
        print "What a great view"
        return True

    # You're actions
    if options.name:
        app.set_name(options.name)

    # Calling the main function
    app.main(args)


if __name__ == "__main__":
    main()
