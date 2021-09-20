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


def add_receipts(user, name, amount, pay, remarks):
    epoch    = round(time())

    data = {
        'Payment-Method': pay,
        'Receipt-Amount': amount,
        'Receipt-Name'  : name,
        'Remarks'       : remarks,
        'epoch'         : epoch,
        'user'          : user,
    }


    db.reference(f'Accounts/Receipts/{user}-{epoch}/').set(data)

