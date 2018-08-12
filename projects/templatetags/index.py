from django import template
register = template.Library()

@register.filter(name='inte')
def inte(i):
    return int(i)

