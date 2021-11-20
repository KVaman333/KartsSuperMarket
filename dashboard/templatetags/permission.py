from functions.permissions import permissions_dic as permissions
from django import template

register = template.Library()

#  CEO  == Cheif Executive Officer       | GM   == General Manager       | SM == Store Manager  |
#  RSO  == Register Sales Officer        | ISO  == InStore Sales Officer | 
#  IIC  == InStore Inventory Coordinator | IM   == Inventory Manager     | SC == Scan Coordinator |
#  HK   == House Keeping                 | MO   == Maintenance Officer   | 
#  HO   == Head Office                   |

@register.filter(name="allow_ho")
def allow_ho(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['HO']:
        return True
    else:
        return False

@register.filter(name="allow_receipts")
def allow_receipts(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['Receipts']:
        return True
    else:
        return False

@register.filter(name="allow_iwoff")
def allow_iwoff(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['IWOff']:
        return True
    else:
        return False

@register.filter(name="allow_pc")
def allow_pc(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['Petty Cash']:
        return True
    else:
        return False

@register.filter(name="allow_po")
def allow_po(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['P.O.']:
        return True
    else:
        return False

@register.filter(name="allow_inventory")
def allow_inventory(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['View Inventory']:
        return True
    else:
        return False

@register.filter(name="allow_notice")
def allow_notice(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['Notice']:
        return True
    else:
        return False

@register.filter(name="allow_cashier")
def allow_cashier(value):
    jobProfile = value.split(':')[3]
    if jobProfile in permissions['Cashier']:
        return True
    else:
        return False


@register.filter(name="allow_sc")
def allow_cashier(value):
    jobProfile = value.split(':')[3]
    if jobProfile in ['SC']:
        return True
    else:
        return False


