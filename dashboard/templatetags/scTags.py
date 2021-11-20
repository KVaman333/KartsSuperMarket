from django import template

register = template.Library()

@register.filter(name="scUser")
def scUser(item, database):
    response = database[item]['user']
    return response

@register.filter(name="scBranch")
def scBranch(item, database):
    response = database[item]['branch']
    return response

@register.filter(name="scInvoiceId")
def scInvoiceId(item, database):
    response = database[item]['invoiceId']
    return response

@register.filter(name="scNoItem")
def scNoItem(item, database):
    response = database[item]['noitem']
    return response

@register.filter(name="scBreakage")
def scBreakage(item, database):
    response = database[item]['breakage']
    return response

@register.filter(name="scDamaged")
def scDamaged(item, database):
    response = database[item]['damaged']
    return response

@register.filter(name="scShortage")
def scShortage(item, database):
    response = database[item]['shortage']
    return response

@register.filter(name="scRemarks")
def scRemarks(item, database):
    response = database[item]['remarks']
    return response

@register.filter(name="scUuid")
def scUuid(item, database):
    response = database[item]['uuid']
    return response
