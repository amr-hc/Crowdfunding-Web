from django_filters import rest_framework as filters

from api.models import Project


class ProjectModelFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Project
        fields = ['title','tages','category']