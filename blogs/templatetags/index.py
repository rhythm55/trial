from django import template
register = template.Library()

@register.filter(name='inte')
def inte(i):
    return int(i)

@register.filter(name='sort')
def sort(list):
    return sorted(list, key=lambda item: getattr(item,'pub_date'))