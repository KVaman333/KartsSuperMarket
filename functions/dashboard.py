from firebase_admin import db




def gr_get(po_num):

    database = db.reference('Orders')
    database = database.get()

    keys_list = database.keys()

    valid     = False
    po_amount = ''
    vendor    = ''

    for key_org in keys_list:
        key = key_org.split(':')
        key = key[-1]
        if key == po_num:
            valid     = True
            po_amount = database[key_org]['poamount']
            vendor    = database[key_org]['vendor']
            break
        else:
            pass



    return valid, po_amount, vendor


def update_goods_receipt(po_num, invoice_amt, invoice_no, remark):

    database = db.reference('Orders')
    database = database.get()

    keys_list = database.keys()

    for key_org in keys_list:
        key = key_org.split(':')
        key = key[-1]
        if key == po_num:
            database = db.reference(f'Orders/{key_org}/')
            database = database.get()

            database['invoiceamt']    = invoice_amt
            database['invoiceno']     = invoice_no
            database['invoiceremark'] = remark

            db.reference(f'Orders/{key_org}/').set(database)
            
        else:
            pass




