from django.core.files.storage import default_storage
from firebase_admin import db, storage
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


def add_receipt_file(file_name, file_path):
    bucket = storage.bucket()

    blob = bucket.blob(f'receipts/{file_name}')
    blob.upload_from_filename(file_path)
    blob.make_public()

    return blob.public_url


def add_receipts(user, name, amount, pay, remarks, file_name):
    epoch = round(time())

    receiptID = get_receipt_id()

    file = file_name.split('.')[-1]
    file = f'{receiptID}.{file}'

    path = add_receipt_file(file, f'media/{file_name}')
    default_storage.delete(file_name)

    data = {
        'Payment-Method': pay,
        'Receipt-Amount': amount,
        'Receipt-ID'    : receiptID,
        'Receipt-Name'  : name,
        'Remarks'       : remarks,
        'epoch'         : epoch,
        'File-Path'     : path,
        'user'          : user,
    }


    db.reference(f'Accounts/Receipts/{user}-{epoch}-{receiptID}/').set(data)

    return receiptID


def add_pc(amount, account, to, by, remarks, user):
    epoch = round(time())

    database = db.reference('Accounts/Petty-Cash/')
    database = database.get()

    keys_list = database.keys()

    id = None

    for key in keys_list: id = key

    if id == 'aaaa-aaaa-aaaa': id = '10000'
    else: id = str(int(id.split('-')[-1]) + 1)

    data = {
        'id'      : id,
        'to'      : to,
        'by'      : by,
        'user'    : user,
        'epoch'   : epoch,
        'Amount'  : amount,
        'Remarks' : remarks,
        'Account' : account,
    }

    db.reference(f'Accounts/Petty-Cash/{user}-{epoch}-{id}').set(data)

    return id

