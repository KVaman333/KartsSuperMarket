from firebase_admin import db
import time



def validate_cookie(request):
    cookie = request.COOKIES.get('user', False)
    if cookie:
        return True
    else:
        return False

def validate_admin(request):
    cookie_user = request.COOKIES.get('user', None)
    database = db.reference(f'Users/{cookie_user}/')
    database = database.get()
    if database['category'] == 'admin':
        return True
    else:
        return False

def get_cookie_user(request):
    cookie_user = request.COOKIES.get('user', None)
    return cookie_user


def user_auth(user_name, user_password):
    database = db.reference('Users')
    database = database.get()

    keys_list = database.keys()
    verified  = False

    for key in keys_list:
        if key == user_name and user_password == database[key]['password']:
            verified = True
        else:
            pass


    return verified


def change(user_name, new_password):
    database = db.reference(f'Users/{user_name}/')
    database = database.get()

    database['password'] = new_password

    db.reference(f'Users/{user_name}/').set(database)


def if_empty(value, substitute):
    if value != None and value != '':
        return value
    else:
        return substitute


def get_time(command):
    epoch = time.localtime()
    if command == 'year':
        return epoch.tm_year
    elif command == 'month':
        return epoch.tm_mon
    elif command == 'mday':
        return epoch.tm_mday
    elif command == 'date':
        return f'{epoch.tm_mon}-{epoch.tm_mday}-{epoch.tm_year}'
    else:
        return epoch
