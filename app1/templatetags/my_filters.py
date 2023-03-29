from django import template
from django.forms.widgets import Widget
register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})


@register.filter(name='add_class1')
def add_class1(value, css_class):
    if isinstance(value, Widget):
        return value.as_widget(attrs={'class': css_class})
    return value