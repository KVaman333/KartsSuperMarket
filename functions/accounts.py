from firebase_admin import db
from time import time



def add_wo(user, event, name, upc, size, quantity, prize, remarks):
    epoch    = round(time())

    data = {
        'Event'      : event,
        'Item-Name'  : name,
        'Pack-Size'  : size,
        'Quantity'   : quantity,
        'Remarks'    : remarks,
        'Total-Price': str(int(quantity)*float(prize)),
        'epoch'      : epoch,
        'upc'        : upc,
        'user'       : user,
    }


    db.reference(f'Accounts/Write-Off/{user}-{epoch}/').set(data)


def get_receipt_id():

    database = db.reference('Accounts/Receipts/')
    database = database.get()

    keys_list = database.keys()

    id = None

    for key in keys_list: id = key

    if id == 'aaaa-aaaa-aaaa': id = '10000'
    else: id = str(int(id.split('-')[-1]) + 1)

    return id


def add_receipts(user, name, amount, pay, remarks):
    epoch = round(time())

    receiptID = get_receipt_id()

    data = {
        'Payment-Method': pay,
        'Receipt-Amount': amount,
        'Receipt-ID'    : receiptID,
        'Receipt-Name'  : name,
        'Remarks'       : remarks,
        'epoch'         : epoch,
        'user'          : user,
    }


    db.reference(f'Accounts/Receipts/{user}-{epoch}-{receiptID}/').set(data)

    return receiptID

