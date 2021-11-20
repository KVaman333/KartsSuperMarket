from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls      import reverse
from firebase_admin   import db


#?  MAIN FUNCTIONS  ?#

def getEditReport(request, *args, **kwargs): # requestHandler/reports/scHandler/
    if request.is_ajax():
        id     = request.GET.get('requestId', False)
        branch = getBranch(request.GET.get('requestcookie', False).split(':')[0])
        data   = getScReportById(id, branch)
        if id != False:
            response = {
                'response' : id,
                'invoiceId': data['invoiceId'],
                'noitem'   : data['noitem'],
                'breakage' : data['breakage'],
                'damaged'  : data['damaged'],
                'shortage' : data['shortage'],
                'remarks'  : data['remarks'],
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                'response': False,
            }
            return JsonResponse(response, status=500)
    else:
        return redirect(reverse('homepage'))


#!  FUNCTION EXTENSIONS  !#

def getBranch(username):
    database = db.reference('Users/')
    database = database.get()
    response = database[username]['branch']
    del database
    return response

def getScReportById(id, branch):
    database = db.reference(f'Management/{branch}/Reports/Inventory/ScanCoordinator/{id}/')
    database = database.get()
    return database