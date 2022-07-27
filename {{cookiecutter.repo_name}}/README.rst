{{cookiecutter.human_name}}
==========================

This is a plugin for `netbox`_. 

Development setup
-----------------

1. Make sure that you have a working `netbox development setup`_.

2. Clone this repository, eg to ``local/{{ cookiecutter.repo_name }}``.

3. Activate the virtual environment you use for netbox development.

4. Execute ``pip install -e .`` within this directory to register this application with netbox's plugin registry.

5. Add the plugin to ``PLUGINS`` in ``configuration.py`` in netbox.

6. Restart your local netbox server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

Copyright {% now 'utc', '%Y' %} {{cookiecutter.author_name}}

Released under the terms of the Apache License 2.0


.. _netbox: https://github.com/netbox-community/netbox
.. _netbox development setup: https://docs.netbox.dev/en/stable/development/getting-started/
