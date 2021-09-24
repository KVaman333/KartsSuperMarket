from django import template
import time

register = template.Library()


##  VIEW RECEIPT FUNCTIONS  ##
@register.filter(name="get_pay")
def get_pay(item, database):
    return database[item]['Payment-Method']

@register.filter(name="get_amount")
def get_amount(item, database):
    return database[item]['Receipt-Amount']

@register.filter(name="get_id")
def get_id(item, database):
    return database[item]['Receipt-ID']

@register.filter(name="get_name")
def get_name(item, database):
    return database[item]['Receipt-Name']

@register.filter(name="get_remarks")
def get_remarks(item, database):
    return database[item]['Remarks']

@register.filter(name="get_path")
def get_path(item, database):
    return database[item]['File-Path']

@register.filter(name="get_time")
def get_time(item, database):
    epoch  = database[item]['epoch']
    result = time.localtime(int(epoch))
    return f'{result.tm_hour}:{result.tm_min}:{result.tm_sec}  {result.tm_mon}-{result.tm_mday}-{result.tm_year}'

@register.filter(name="get_user")
def get_user(item, database):
    return database[item]['user']


##  VIEW INVOICES FUNCTIONS  #
    