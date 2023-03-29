import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from .models import *
from django import forms

class DepartmentFilter(django_filters.FilterSet):
    id = NumberFilter(field_name='id')
    name = CharFilter(field_name='name', lookup_expr='icontains', label='Dept Name')
    location = CharFilter(field_name='location', lookup_expr='icontains', widget=forms.Select(choices=[('', 'All Blocks')] + list(Department.LOCATION)))
    rank = NumberFilter(field_name='rank')
    phone = CharFilter(field_name='phone',lookup_expr='icontains')
    email = CharFilter(field_name='email',lookup_expr='icontains')
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')

    class Meta:
        model = Department
        fields = ['id', 'name', 'location', 'rank', 'phone', 'email', 'start_date']
        exclude = ['date_created', 'description']