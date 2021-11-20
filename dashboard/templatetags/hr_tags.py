from functions.permissions import permissions_abrevation as abs
from django import template

register = template.Library()



@register.filter(name="get_id")
def get_id(item, database):
    response = database[item]['id']
    return response

@register.filter(name="get_name")
def get_name(item, database):
    response = database[item]['name']
    return response

@register.filter(name="get_email")
def get_email(item, database):
    response = database[item]['mail']
    return response

@register.filter(name="get_profile")
def get_profile(item, database):
    response = database[item]['id']
    return response

@register.filter(name="get_job")
def get_profile(item, database):
    response = database[item]['job_profile']
    response = abs[response]
    return response


##  PROFILE TEMPLETE TAGS  ##



@register.filter(name="pro_name")
def pro_name(database):
    response = database['name']
    return response

@register.filter(name="pro_job")
def pro_job(database):
    response = database['job_profile']
    response = abs[response]
    return response

@register.filter(name="pro_email")
def pro_email(database):
    response = database['mail']
    return response

@register.filter(name="pro_address")
def pro_address(database):
    response = database['address']
    return response

@register.filter(name="pro_phone")
def pro_phone(database):
    response = database['phone']
    return response

@register.filter(name="pro_refn1")
def pro_job(database):
    response = database['ref_name1']
    return response

@register.filter(name="pro_refn2")
def pro_job(database):
    response = database['ref_name2']
    return response

@register.filter(name="pro_refp1")
def pro_job(database):
    response = database['ref_phone1']
    return response

@register.filter(name="pro_refp2")
def pro_job(database):
    response = database['ref_phone2']
    return response


