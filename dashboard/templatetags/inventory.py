from django import template

register = template.Library()


@register.filter(name="get_locator")
def get_locator(item, database):
    return database[item]['STOCK LOCATOR']

@register.filter(name="get_vendorid")
def get_vendorid(item, database):
    return database[item]['ITEM ORDER']

@register.filter(name="get_description")
def get_description(item, database):
    return database[item]['DESCRIPTION']

@register.filter(name="get_qty")
def get_qty(item, database):
    return database[item]['QTY']

@register.filter(name="get_sell")
def get_sell(item, database):
    return database[item]['PRICE SELL']

@register.filter(name="get_upc")
def get_upc(item, database):
    return database[item]['UPC']

# @register.filter(name="get_locator")
# def get_locator(item, database):
#     return database[item]['Stock Locator']

# @register.filter(name="get_locator")
# def get_locator(item, database):
#     return database[item]['Stock Locator']

# @register.filter(name="get_locator")
# def get_locator(item, database):
#     return database[item]['Stock Locator']


