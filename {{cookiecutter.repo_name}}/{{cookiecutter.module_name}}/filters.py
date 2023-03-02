# import django_filters
# from django.db.models import Q
# from extras.filters import TagFilter
# from netbox.filtersets import NetBoxModelFilterSet

# from .models import MyModel


# class MyModelFilterSet(NetBoxModelFilterSet):
#     q = django_filters.CharFilter(
#         method='search',
#         label='Search',
#     )
#     tag = TagFilter()

#     class Meta:
#         model = MyModel
#         fields = ['something', 'other']

#     def search(self, queryset, name, value):
#         """Perform the filtered search."""
#         if not value.strip():
#             return queryset
#         qs_filter = (
#                 Q(id__icontains=value)
#                 | Q(value__icontains=value)
#                 | Q(description__icontains=value)
#         )
#         return queryset.filter(qs_filter)
