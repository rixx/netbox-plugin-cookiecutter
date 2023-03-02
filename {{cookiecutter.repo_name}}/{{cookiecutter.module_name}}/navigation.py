# from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
# from utilities.choices import ButtonColorChoices


# _menu_items = (
#     PluginMenuItem(
#         link='plugins:{{cookiecutter.module_name}}:mymodel_list',
#         link_text='MyModel',
#         permissions=['{{cookiecutter.module_name}}.view_mymodel'],
#         buttons=(
#             PluginMenuButton(
#                 link='plugins:{{cookiecutter.module_name}}:mymodel_add',
#                 title='MyModel',
#                 icon_class='mdi mdi-plus-thick',
#                 color=ButtonColorChoices.GREEN,
#                 permissions=['{{cookiecutter.module_name}}.add_mymodel'],
#             ),
#         ),
#     ),
# )


# menu = PluginMenu(  
#     label="{{cookiecutter.repo_name}}",
#     groups=(("{{cookiecutter.repo_name}}", _menu_items),),
#     icon_class="mdi mdi-bootstrap",
# )
