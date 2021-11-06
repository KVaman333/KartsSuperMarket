from django.core.files.storage import default_storage
from firebase_admin import db, storage



def gr_get(po_num):

    database = db.reference('Orders')
    database = database.get()

    keys_list = database.keys()

    valid     = False
    po_amount = ''
    vendor    = ''

    for key_org in keys_list:
        key = key_org.split(':')
        key = str(int(key[-1]))
        if key == po_num:
            valid     = True
            po_amount = database[key_org]['poamount']
            vendor    = database[key_org]['vendor']
            break
        else:
            pass



    return valid, po_amount, vendor


def add_invoice_file(file_name, file_path):
    bucket = storage.bucket()

    blob = bucket.blob(f'invoices/{file_name}')
    blob.upload_from_filename(file_path)
    blob.make_public()

    return blob.public_url


def update_goods_receipt(po_num, invoice_amt, invoice_no, remark, file_name, user):

    database = db.reference('Orders')
    database = database.get()

    keys_list = database.keys()

    for key_org in keys_list:
        key = key_org.split(':')
        key = str(int(key[-1]))
        if key == po_num:
            database = db.reference(f'Orders/{key_org}/')
            database = database.get()

            file = file_name.split('.')[-1]
            file = f'{po_num}.{file}'

            path = add_invoice_file(file, f'media/{file_name}')
            default_storage.delete(file_name)

            database['invoiceamt']    = invoice_amt
            database['invoiceno']     = invoice_no
            database['invoiceremark'] = remark
            database['file-path']     = path
            database['receivedby']    = user

            db.reference(f'Orders/{key_org}/').set(database)
            break
            
        else:
            pass


def editable_po(po_num):
    database = db.reference('Orders')
    database = database.get()

    keys_list = database.keys()
    valid     = False

    for key_org in keys_list:
        key = key_org.split(':')
        key = str(int(key[-1]))
        if key == po_num and database[key_org]['invoiceno'] == '':
            valid = True
            break
        else:
            pass

    return valid


def get_notices(user):
    userbase = db.reference(f'Users/{user}/')
    userbase = userbase.get()
    branch   = userbase['branch']
    database = db.reference(f'Accounts/Notice/{branch}/')
    database = database.get()

    del database['0000-0000-0000']

    return database
