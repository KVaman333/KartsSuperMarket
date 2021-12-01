from django import template

register = template.Library()


@register.filter(name="get_locator")
def get_locator(item, database):
    if 'stockLocator' in database[item].keys():
        return database[item]['stockLocator']
    else:
        return '#'

@register.filter(name="get_upc")
def get_upc(item, database):
    if 'upc' in database[item].keys():
        return database[item]['upc']
    return '-'

@register.filter(name="get_name")
def get_name(item, database):
    if 'name' in database[item].keys() and '' != database[item]['name']:
        return database[item]['name']
    return '-'

@register.filter(name="get_pack_size")
def get_pack_size(item, database):
    if 'unitP' in database[item].keys() and '' != database[item]['unitP']:
        return database[item]['pack']
    return '-'

@register.filter(name="get_price")
def get_price(item, database):
    if 'price' in database[item].keys() and '' != database[item]['price']:
        return database[item]['unitP']
    return '-'

@register.filter(name="get_quantity")
def get_quantity(item, database):
    if 'quantity' in database[item].keys() and '' != database[item]['quantity']:
        return database[item]['quantity']
    return '-'

@register.filter(name="get_ebt")
def get_ebt(item, database):
    if 'ebt' in database[item].keys() and '' != database[item]['ebt']:
        return database[item]['ebt']
    return '-'

@register.filter(name="if_image")
def if_image(item, database):
    if 'image1' in database[item].keys() and '' != database[item]['image1']:
        return True
    return False

@register.filter(name="get_image")
def get_image(item, database):
    if 'image1' in database[item].keys() and '' != database[item]['image1']:
        return database[item]['image1']
    return '-'

@register.filter(name="get_vendor")
def get_vendor(item, database):
    if 'vendor' in database[item].keys() and '' != database[item]['vendor']:
        return database[item]['vendor']
    return '-'


#  CLASSES FILTERS  #

@register.filter(name="department")
def department(item, database):
    return database[item]['DEPARTMENT']

@register.filter(name="sub_department")
def sub_department(item, database):
    return database[item]['SUB-DEPARTMENT']

@register.filter(name="category")
def category(item, database):
    return database[item]['CATEGORY']

@register.filter(name="id")
def idd(item, database):
    return database[item]['ID']

