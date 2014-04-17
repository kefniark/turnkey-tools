turnkey-tools
========================

A small software to easily manage task on turnkeylinux VM

How to install
-------------------------------------------

For the moment, to install to your turnkey VM

    apt-get install python-setuptools
    easy_install https://github.com/kefniark/turnkey-tools/raw/develop/dist/turnkey_tools-0.0.1-py2.7.egg

How to Use
-------------------------------------------

At this moment, you will get the '''turnkey-tools''' command

    turnkey-tools -h

Functionalities are used as plugin, you can easily enable/disable each turnkey's feature
To list all plugins

    turnkey-tools --list

and for each plugin, you have actions (enable/disable/install/status)

    turnkey-tools webmin disable
    turnkey-tools webmin enable

and if you want something simple

    turnkey-tools all disable