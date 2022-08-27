from django import template

register = template.Library()



@register.filter
def index(dictionary, i):
    i = int(i)-1
    if (i>4):
        i = 4
    i = (i-4)*(-1)
    return dictionary[i]['color']

