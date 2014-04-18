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

Functionalities are used as plugin, you can easily enable/disable each turnkey's feature.
To list all available plugins :

    turnkey-tools --list

The Plugins are for the moment :
    * Webmin
    * Shell in a box
    * PhpMyadmin
    * Monit
    * Firewall

and for each plugin, you have those actions (enable/disable/install/status)
So for a new turnkey installation, I suggest you to execute :

    turnkey-tools webmin disable
    turnkey-tools shellinabox disable
    turnkey-tools firewall enable
    turnkey-tools monit install

and if you want something simple

    turnkey-tools all disable