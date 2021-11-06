from django import template

register = template.Library()


@register.filter(name="get_locator")
def get_locator(item, database):
    return database[item]['STOCK LOCATOR']

@register.filter(name="get_item_order")
def get_item_order(item, database):
    return database[item]['ITEM ORDER']

@register.filter(name="get_description")
def get_description(item, database):
    return database[item]['DESCRIPTION']

@register.filter(name="get_sub_description")
def get_sub_description(item, database):
    return database[item]['SUB-DESCRIPTION']

@register.filter(name="get_vendorid")
def get_vendorid(item, database):
    return database[item]['VENDOR ID']

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

@register.filter(name="get_unit_upc")
def get_unit_upc(item, database):
    if database[item]['UNIT UPC'] == "":
        sell = ""
    else:
        sell = str(round(float(database[item]['UNIT UPC'])))
    return sell

@register.filter(name="get_pack_upc")
def get_pack_upc(item, database):
    if database[item]['PACK UPC'] == "":
        sell = ""
    else:
        sell = str(round(float(database[item]['PACK UPC'])))
    return sell


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

