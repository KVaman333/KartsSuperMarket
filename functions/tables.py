from firebase_admin import db




def stock_inventory():
    database = db.reference('Inventory/Stock/')
    database = database.get()

    return database