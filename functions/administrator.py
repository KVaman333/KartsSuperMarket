from firebase_admin import db



##  ITEM ENTRY FUNTIONS  ##
def add_inventory_items():
    return


def add_notice_items():
    return


##  VIEW DATA FUNCTIONS  ## 
def get_receipts():
    database = db.reference('Accounts/Receipts/')
    database = database.get()

    del database['aaaa-aaaa-aaaa']

    return database


def get_invoices():
    database = db.reference('Orders/')
    database = database.get()

    return database

