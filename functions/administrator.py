from firebase_admin import db
from time import time



##  VIEW DATA FUNCTIONS  ## 
def get_receipts():
    database = db.reference('Accounts/Receipts/')
    database = database.get()

    del database['0000-0000-0000']

    return database


def get_invoices():
    database = db.reference('Orders/')
    database = database.get()

    return database


def add_inventory_item(stock_locator, item_order, description, sub_description, vendor_id, unit_upc, pack_upc, buy, sell, qty, department):
    database = db.reference('Inventory/Stock/')
    database = database.get()

    keys_list = database.keys()


    if len(stock_locator) == 1:stock_locator = f'000{stock_locator}'
    elif len(stock_locator) == 2:stock_locator = f'00{stock_locator}'
    elif len(stock_locator) == 3:stock_locator = f'0{stock_locator}'
    else:pass

    if stock_locator not in keys_list:
        data = {
            'STOCK LOCATOR'  : stock_locator,
            'ITEM ORDER'     : item_order,
            'DESCRIPTION'    : description,
            'SUB-DESCRIPTION': sub_description,
            'VENDOR ID'      : vendor_id,
            'UNIT UPC'       : unit_upc,
            'PACK UPC'       : pack_upc,
            'PRICE BUY'      : buy,
            'PRICE SELL'     : sell,
            'QTY'            : qty,
            'DEPARTMENT'     : department,
        }


        db.reference(f'Inventory/Test/{stock_locator}/').set(data)

        return True
    else:
        return False


def except_pack_upc(request): 
    response = False
    for i in request.POST:
        if i != 'pack_upc' and request.POST[i] != '':
            response = True
        else:
            pass
    return response


def add_notice(title, text, user):
    epoch = round(time())

    userbase = db.reference(f'Users/{user}/')
    userbase = userbase.get()
    branch   = userbase['branch']
    database = db.reference(f'Accounts/Notice/{branch}/')
    database = database.get()
    del userbase

    keys_list = database.keys()
    del database

    id = None

    for key in keys_list: id = key
    del keys_list

    if id == '0000-0000-0000': id = '100000'
    else: id = str(int(id.split('-')[-1]) + 1)

    data = {
        'branch'  : branch,
        'id'      : id,
        'title'   : title,
        'text'    : text,
        'user'    : user,
        'epoch'   : epoch,
    }

    db.reference(f'Accounts/Notice/{branch}/{epoch}-{id}').set(data)

    return id
