""" Use this file to expand core views.

from extras.plugins import PluginTemplateExtension

class ExtraContent(PluginTemplateExtension):
    model = 'dcim.site'  # insert your model here

    # read more about available methods here:
    # https://docs.netbox.dev/en/stable/plugins/development/views/#extending-core-views
    def right_page(self):
        return self.render('{{ cookiecutter.module_name }}/dcim_right_page.html', extra_context={
            'foo': 'bar',
        })
"""
template_extensions = []
