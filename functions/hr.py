from firebase_admin import db
from time import time

#  vamiw:Vaman:god@mail.com:GM

def create_employee(employee_details):
    try:
        database = db.reference('Human-Resources/')
        database = database.get()
        epoch = round(time(), 2)

        keys_list = list(database.keys())

        if keys_list[-1] == '0000': id = '1000'
        else: id = str(int(keys_list[-1])+1)

        employee_details['id']    = id
        employee_details['epoch'] = epoch

        db.reference(f'Human-Resources/{id}/').set(employee_details)
        return True

    except Exception as error: 
        print(f'[{error}]')
        return False

def employee_datatable():
    database = db.reference('Human-Resources/Employees/')
    database = database.get()

    del database['0000']

    return database

def employee_profile(id):
    database = db.reference(f'Human-Resources/Employees/{id}/')
    database = database.get()

    return database