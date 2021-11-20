from functions.authentication import validate_cookie
from functions.permissions    import allow_profile
from django.shortcuts import redirect, render
from django.urls      import reverse
from firebase_admin   import db

#!  VARIABLES  #
JOB_PROFILE = ['CEO','GM','SC']
FORM_FIELDS = ['invoiceId', 'noItem', 'breakage', 'damaged', 'shortage', 'remarks']

def form(request, *args, **kwargs): # URL == dashboard/daily-reports/Scan-Coordinator/form/
    if validate_cookie(request):
        if allow_profile(request, JOB_PROFILE):
            if 'error' in kwargs:
                user   = getUsername(request)
                branch = getBranch(user)
                data   = getReports(user, branch)
                ginger = {
                    'invalidDetails': True,
                    'database': data
                }
                return render(request, 'forms/scForm.html', ginger)
            if request.method == 'POST':
                if all(item in request.POST and request.POST[item] != '' for item in FORM_FIELDS):
                    if confirmInvoiceID(request.POST['invoiceId']):
                        return redirect(f"/./dashboard/daily-reports/Scan-Coordinator/create/{request.POST['invoiceId']}/{request.POST['noItem']}/{request.POST['breakage']}/{request.POST['damaged']}/{request.POST['shortage']}/{request.POST['remarks']}/")
                    else:
                        user   = getUsername(request)
                        branch = getBranch(user)
                        data   = getReports(user, branch)
                        ginger = {
                            'invalidDetails': True,
                            'database'      : data,
                        }
                        return render(request, 'forms/scForm.html', ginger)
                else:
                    user   = getUsername(request)
                    branch = getBranch(user)
                    data   = getReports(user, branch)
                    ginger = {
                        'invalidDetails': True,
                        'database'      : data,
                    }
                    return render(request, 'forms/scForm.html', ginger)
            else:
                user   = getUsername(request)
                branch = getBranch(user)
                data   = getReports(user, branch)
                ginger = {
                    'database': data
                }
                return render(request, 'forms/scForm.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))

def create(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_profile(request, JOB_PROFILE):
            if list(kwargs.keys()) == FORM_FIELDS:
                user   = getUsername(request)
                data = {
                    'user'      : user,
                    'branch'    : getBranch(user),
                    'invoiceId' : kwargs['invoiceId'],
                    'noitem'    : kwargs['noItem'],
                    'breakage'  : kwargs['breakage'],
                    'damaged'   : kwargs['damaged'],
                    'shortage'  : kwargs['shortage'],
                    'remarks'   : kwargs['remarks'],
                }
                response = createReport(data)
                if response == 'INVALID':
                    return redirect('/./dashboard/daily-reports/Scan-Coordinator/form/invalid-invoiceId/')
                elif not response:
                    return redirect(reverse('se'))
                else:
                    return redirect(reverse('scForm'))
            else:
                return redirect(reverse('scForm'))
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


#H1  REDIRECT FUNCTIONS  #
from time import time

def getReports(user, branch):
    database = db.reference(f'Management/{branch}/Reports/Inventory/ScanCoordinator/')
    database = database.get()
    del database['00000']

    keys_list = list(database.keys())

    response = {}

    for key in keys_list:
        if database[key]['user'] == user and database[key]['branch'] == branch:
            if checkEpoch(float(database[key]['epoch'])):
                response[key] = database[key]
            else:
                pass
        else:
            pass

    return response

def createReport(data):
    try:
        epoch = round(time())
        database  = db.reference(f"Management/{data['branch']}/Reports/Inventory/ScanCoordinator/")
        database  = database.get()
        del database['00000']
        keys_list = database.keys()

        update = False
        for key in keys_list:
            print(getToday())
            if getToday() > float(database[key]['epoch']):
                return 'INVALID'
            if database[key]['invoiceId'] == data['invoiceId']:
                id     = key
                update = True
                break
            id = key
        
        if id == '00000': id = '10000'
        elif update : pass
        else: id = str(int(id.split('-')[-1]) + 1)

        data['uuid']  = id
        data['epoch'] = epoch

        db.reference(f"Management/{data['branch']}/Reports/Inventory/ScanCoordinator/{id}/").set(data)
        return True
    except Exception as error:
        print(f'[ SCAN-COORDINATOR CREATE-REPORT ] : [{error}]')
        return False


#H3  FUNCTIONS  #
from datetime import datetime, timezone

def getUsername(request):
    cookie_user = request.COOKIES.get('user', None)
    cookie_user = cookie_user.split(':')[0]
    return cookie_user

def getBranch(username):
    database = db.reference('Users/')
    database = database.get()
    response = database[username]['branch']
    return response

def confirmInvoiceID(ID):
    database  = db.reference('Orders/')
    database  = database.get()
    keys_list = database.keys()
    
    response = False
    for key in keys_list:
        if ID == key.split(':')[1]:
            response = True
        else:
            pass

    return response

def getToday():
    now   = datetime.now(timezone.utc)
    today = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    return float(today.strftime('%s'))

def getTomorrow():
    now   = datetime.now(timezone.utc)
    today = now.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    tomorrow = int(today.strftime('%s')) + (24*60*60)
    return tomorrow

def checkEpoch(value):
    today    = getToday()
    tomorrow = getTomorrow()
    if float(today) < float(value) < float(tomorrow):
        return True
    else:
        return False

