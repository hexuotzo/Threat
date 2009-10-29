from django import template

register = template.Library()

@register.filter
def torf(text):
    if text=="False":
        return "√"
    elif text=="True":
        return "x"
