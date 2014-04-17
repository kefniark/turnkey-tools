#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Your application """

class Application:

    def __init__(self):
        self.name = "myapp"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def main(self):
        print "Your app is named : %s " % (self.name,)


#just for development
if __name__ == "__main__":
    app = Application()
    app.main()
