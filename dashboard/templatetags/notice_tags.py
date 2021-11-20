from functions.authentication import get_username_name
from django import template
import time

register = template.Library()

def digits_num(string):
    dig = str(string)
    if len(dig) == 1:
        return f'0{dig}'
    else:
        return dig

@register.filter(name="get_title")
def get_name(notice, database):
    response = database[notice]['title']
    return response

@register.filter(name="get_text")
def get_email(notice, database):
    response = database[notice]['text']
    return response

@register.filter(name="get_user_name")
def get_user(notice, database):
    response = get_username_name(database[notice]['user'])
    return response

@register.filter(name="get_time")
def get_time(notice, database):
    epoch  = database[notice]['epoch']
    result = time.localtime(int(epoch))

    hour = digits_num(result.tm_hour)
    min  = digits_num(result.tm_min)
    sec  = digits_num(result.tm_sec)
    mon  = digits_num(result.tm_mon)
    day  = digits_num(result.tm_mday)
    year = digits_num(result.tm_year)

    return f'{hour}:{min}:{sec}  {mon}-{day}-{year}'