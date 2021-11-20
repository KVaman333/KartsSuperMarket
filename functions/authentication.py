from firebase_admin import db
import time



def validate_cookie(request):
    cookie = request.COOKIES.get('user', 'False')
    cookie = cookie.split(':')[0]
    if cookie != 'False':
        return True
    else:
        return False

def create_cookie(response, request_username):
    database = db.reference(f'Users/{request_username}/')
    database = database.get()
    data     = f"{request_username}:{database['name']}:{database['email']}:{database['category']}"
    response.set_cookie('user', data)
    return response


def get_cookie_user(request):
    cookie_user = request.COOKIES.get('user', None)
    cookie_user = cookie_user.split(':')[0]
    return cookie_user

def user_auth(user_name, user_password):
    database = db.reference('Users')
    database = database.get()

    keys_list = database.keys()
    verified  = False

    for key in keys_list:
        if key == user_name and user_password == database[key]['password']:
            verified = True
            data = {
                'status': 'ACTIVE'
            }
            db.reference(f'Human-Resources/Active-Users/{user_name}/').set(data)
            break
        else:
            pass

    return verified

def user_logout(request, response):
    user   = get_cookie_user(request)
    response.delete_cookie('user')
    db.reference(f'Human-Resources/Active-Users/{user}/').delete()
    return response


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


def get_username_name(username):
    userbase  = db.reference(f'Users/{username}/')
    userbase  = userbase.get()
    user_name = userbase['name']
    
    return user_name
