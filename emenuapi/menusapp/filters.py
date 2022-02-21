from django_filters import rest_framework as filters
from .models import Menu

class MenuFilter(filters.FilterSet):
    class Meta:
        model = Menu
        fields = ['name', 'added', 'modified']
