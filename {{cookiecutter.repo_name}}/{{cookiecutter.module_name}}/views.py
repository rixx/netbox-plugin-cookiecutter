# from netbox.views import generic

# from .models import MyModel
# from . import forms, tables, filters


# class MyModelListView(generic.ObjectListView):
#     queryset = MyModel.objects.all()
#     filterset = filters.MyModelFilterSet
#     filterset_form = forms.MyModelFilterForm
#     table = tables.MyModelTable
#     action_buttons = ('add',)


# class MyModelView(generic.ObjectView):
#     queryset = MyModel.objects.all()
#     template_name = '{{cookiecutter.module_name}}/mymodel.html'


# class MyModelEditView(generic.ObjectEditView):
#     queryset = MyModel.objects.all()
#     form = forms.MyModelForm


# class MyModelBulkDeleteView(generic.BulkDeleteView):
#     queryset = MyModel.objects.all()
#     table = tables.MyModelTable


# class MyModelBulkEditView(generic.BulkEditView):
#     queryset = MyModel.objects.all()
#     filterset = filters.MyModelFilterSet
#     table = tables.MyModelTable
#     form = forms.MyModelBulkEditForm


# class MyModelDeleteView(generic.ObjectDeleteView):
#     queryset = MyModel.objects.all()
#     default_return_url = 'plugins:{{cookiecutter.module_name}}:mymodel_list'
