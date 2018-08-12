from django import template
register = template.Library()

@register.filter(name='index')
def index(List,i):
    return List[int(i)]

@register.filter(name='var')
def var(i):
    return i+1


@register.filter(name='inte')
def inte(i):
    return int(i)

#subtopics|index:subtopic_id

@register.filter(name='length')
def length(list):
    return len(list)