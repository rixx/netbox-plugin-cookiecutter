from extras.plugins import PluginConfig


class {{cookiecutter.module_name.replace("_", "").capitalize()}}PluginConfig(PluginConfig):
    """ Plugin configuration.

    See https://docs.netbox.dev/en/stable/plugins/development/#pluginconfig-attributes
    for a list of all possible attributes."""

    name = "{{cookiecutter.module_name}}"
    verbose_name = "{{cookiecutter.human_name}}"
    description = gettext_lazy("{{cookiecutter.short_description}}")
    author = "{{cookiecutter.author_name}}"
    author_email = "{{cookiecutter.author_email}}"
    version = "0.0.0"
    base_url = "{{cookiecutter.module_name.replace("_", "-")}}"
    required_settings = []
    default_settings = {}

    def ready(self):
        from . import signals  # NOQA



config = {{cookiecutter.module_name.replace("_", "").capitalize()}}PluginConfig
