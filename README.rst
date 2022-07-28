netbox-plugin-cookiecutter
==========================

A simple `cookiecutter`_ template to bootstrap a `netbox`_ plugin.

Usage
-----

Let's pretend you want to create a netbox plugin called "superplugin".
First, create a virtual environment and install the ``cookiecutter``
package using pip. Next, use it to bootstrap your project folder::

    $ cd <your-project-folder-parent>
    $ cookiecutter https://github.com/rixx/netbox-plugin-cookiecutter


You'll be prompted for some questions. Answer them, and you will find a
project folder created for you::

    repo_name [netbox-superplugin]: netbox-superplugin
    repo_url [GitHub repository URL]: https://github.com/myuser/netbox-superplugin
    module_name [netbox_superplugin]: netbox_superplugin
    human_name [The netbox super plugin]: Super Plugin
    author_name [Your name]: J Random Developer
    author_email [Your email]: jrandom@example.org
    short_description [Short description]: The best plugin

Now, change to the newly created directory::

    $ cd netbox-superplugin

Voilà, there's your plugin structure! See netbox' `documentation`_ for more info.

------

Work on this project was kindly sponsored by `Globalways`_.

.. image:: https://globalways.net/wp-content/uploads/2020/11/Varianten_Globalways_Logo_Farbe_Globalways_Logo_Farbe_2.svg
   :target: https://globalways.net
   :alt: Globalways logo

.. _netbox: https://github.com/netbox-community/netbox
.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _documentation: https://docs.netbox.dev/en/stable/plugins/development/
.. _globalways: https://www.globalways.net
