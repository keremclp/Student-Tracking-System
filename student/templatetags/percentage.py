from django import template

register = template.Library()

@register.filter
def percentage(value, arg):
    if arg == 0:
        return 0
    return int((value/arg)*100)