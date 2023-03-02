# import django_tables2 as tables

# from netbox.tables import NetBoxTable
# from netbox.tables.columns import ChoiceFieldColumn, TagColumn

# from .models import MyModel

# class MyModelTable(NetBoxTable):
#     something = tables.LinkColumn()
#     choice_field = ChoiceFieldColumn()
#     tags = TagColumn(url_name='plugins:{{cookiecutter.module_name}}:mymodel_list')

#     class Meta(NetBoxTable.Meta):
#         model = MyModel
#         fields = ('pk', 'something', 'choice_field', 'tags')
#         default_columns = fields
