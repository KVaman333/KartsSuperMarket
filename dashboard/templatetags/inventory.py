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
    if database[item]['QTY'] == "":
        qty = ""
    else:
        qty = str(round(float(database[item]['QTY'])))
    return qty

@register.filter(name="get_sell")
def get_sell(item, database):
    if database[item]['PRICE SELL'] == "":
        sell = ""
    else:
        sell = str(round(float(database[item]['PRICE SELL']), 2))
    return sell

@register.filter(name="get_upc")
def get_upc(item, database):
    if database[item]['UPC'] == "":
        sell = ""
    else:
        sell = str(round(float(database[item]['UPC'])))
    return sell

# @register.filter(name="get_locator")
# def get_locator(item, database):
#     return database[item]['Stock Locator']

# @register.filter(name="get_locator")
# def get_locator(item, database):
#     return database[item]['Stock Locator']

# @register.filter(name="get_locator")
# def get_locator(item, database):
#     return database[item]['Stock Locator']


