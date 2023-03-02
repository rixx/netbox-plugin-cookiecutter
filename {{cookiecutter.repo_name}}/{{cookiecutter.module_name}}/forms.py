# from django import forms

# from extras.models import Tag
# from utilities.forms import (
#     DynamicModelMultipleChoiceField, StaticSelect,
#     StaticSelectMultiple, TagFilterField
# )
# from netbox.forms import NetBoxModelForm, NetBoxModelBulkEditForm, NetBoxModelFilterSetForm

# from .models import MyModel


# class MyModelForm(NetBoxModelForm):
#     tags = DynamicModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         required=False
#     )

#     class Meta:
#         model = MyModel
#         fields = ['something', 'tags']


# class MyModelFilterForm(NetBoxModelFilterSetForm):
#     q = forms.CharField(
#         required=False,
#         label='Search'
#     )
#     tag = TagFilterField(MyModel)

#     model = MyModel


# class MyModelBulkEditForm(NetBoxModelBulkEditForm):
#     pk = forms.ModelMultipleChoiceField(
#         queryset=MyModel.objects.all(),
#         widget=forms.MultipleHiddenInput
#     )
#     description = forms.CharField(
#         max_length=200,
#         required=False
#     )

#     model = MyModel
#     nullable_fields = ['description', ]
