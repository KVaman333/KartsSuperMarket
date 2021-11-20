from firebase_admin import db

#  CEO  == Cheif Executive Officer       | GM   == General Manager       | SM   == Store Manager  |
#  RSO  == Register Sales Officer        | ISO  == InStore Sales Officer | 
#  IIC  == InStore Inventory Coordinator | IM   == Inventory Manager     | SC == Scan Coordinator |
#  HK   == House Keeping                 | MO   == Maintenance Officer   | 
#  HO   == Head Office                   |

permissions_abrevation = { # CEO, GM, SM == ABSOLUTE
    'GM' : 'General Manager',
    'SM' : 'Store Manager',
    'IM' : 'Inventory Manager',
    'SC' : 'Scan Coordinator',
    'HK' : 'House Keeping',
    'MO' : 'Maintenance Officer',
    'HO' : 'Head Office',
    'CEO' : 'Cheif Executive Officer',
    'RSO' : 'Register Sales Officer',
    'ISO' : 'InStore Sales Officer',
    'IIC' : 'InStore Inventory Coordinator',
}

permissions_dic = { # CEO, GM, SM == ABSOLUTE
    'A'                   : ['CEO','GM','SM'],
    'HO'               : ['CEO','GM'],
    'Receipts'         : ['CEO','GM','SM'],
    'Cashier'          : ['CEO','GM','SM', 'RSO'],
    'IWOff'            : ['CEO','GM','SM'],
    'Petty Cash'       : ['CEO','GM','SM'],
    'P.O.'             : ['CEO','GM','SM', 'IM', 'SC'],
    'View Inventory'   : ['CEO','GM','SM', 'RSO', 'ISO', 'IIC', 'IM', 'SC'],
    'View Departments' : ['CEO','GM','SM', 'RSO', 'ISO', 'IIC', 'IM', 'SC'],
    'Notice'           : ['CEO','GM','SM'],
}

def get_cookie(request):
    cookie = request.COOKIES.get('user', 'Anonymous')
    return cookie


def allow_A(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['A']:
        return True
    else:
        return False

def allow_ho(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['HO']:
        return True
    else:
        return False

def allow_receipts(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['Receipts']:
        return True
    else:
        return False

def allow_iwoff(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['IWOff']:
        return True
    else:
        return False

def allow_pc(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['Petty Cash']:
        return True
    else:
        return False

def allow_po(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['P.O.']:
        return True
    else:
        return False

def allow_inventory(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['View Inventory']:
        return True
    else:
        return False

def allow_notice(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['Notice']:
        return True
    else:
        return False

def allow_cashier(request):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in permissions_dic['Cashier']:
        return True
    else:
        return False

def allow_profile(request, jobProfile):
    value = get_cookie(request)
    response = value.split(':')[3]
    if response in jobProfile:
        return True
    else:
        return False
