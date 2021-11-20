from django import template

register = template.Library()

@register.filter(name="name")
def get_name(value):
    response = value.split(':')[1]
    return response

@register.filter(name="email")
def get_email(value):
    response = value.split(':')[2]
    return response