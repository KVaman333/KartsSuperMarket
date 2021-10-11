from django import template
import time

register = template.Library()

def digits_num(string):
    dig = str(string)
    if len(dig) == 1:
        return f'0{dig}'
    else:
        return dig

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

    hour = digits_num(result.tm_hour)
    min  = digits_num(result.tm_min)
    sec  = digits_num(result.tm_sec)
    mon  = digits_num(result.tm_mon)
    day  = digits_num(result.tm_mday)
    year = digits_num(result.tm_year)

    return f'{hour}:{min}:{sec}  {mon}-{day}-{year}'

@register.filter(name="get_user")
def get_user(item, database):
    return database[item]['user']


##  VIEW INVOICES FUNCTIONS  #


@register.filter(name="get_iuser")
def get_iuser(item, database):
    return database[item]['entryby']

@register.filter(name="get_ipono_inno")
def get_ipono_inno(item, database):
    response1 = database[item]['pono']
    response2 = database[item]['invoiceno']

    return f'{response1}/{response2}'

@register.filter(name="get_ipoamt")
def get_ipoamt(item, database):
    return database[item]['poamount']

@register.filter(name="get_iinamt")
def get_iinamt(item, database):
    if database[item]['invoiceamt'] != '':
        return f"$ {database[item]['invoiceamt']}"
    else:
        return 'Not Entered'


@register.filter(name="get_ipay")
def get_ipay(item, database):
    if database[item]['paymethod'] != '':
        return database[item]['paymethod']
    else:
        return 'Not Paid'
     
@register.filter(name="get_ivendor")
def get_ivendor(item, database):
    return database[item]['vendor']
     
@register.filter(name="get_ireceivedby")
def get_ireceivedby(item, database):
    if 'receivedby' in database[item].keys() and database[item]['receivedby'] != '':
        return database[item]['receivedby']
    else:
        return 'Not Rcvd'

@register.filter(name="get_iepoch")
def get_iepoch(item, database):
    return database[item]['epoch']

@register.filter(name="if_ifile")
def if_ifile(item, database):
    if 'file-path' in database[item].keys() and database[item]['file-path'] != '':
        return True
    else:
        return False

@register.filter(name="get_ifile")
def get_ifile(item, database):
    return database[item]['file-path']

    