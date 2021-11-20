from functions.authentication  import get_cookie_user, validate_cookie
from functions.hr              import create_employee, employee_datatable, employee_profile
from functions.permissions     import *
from django.shortcuts import redirect, render
from django.urls      import reverse

# Create your views here.

employee_details = ['name', 'age', 'address', 'phone', 'mail', 'ref_name1', 'ref_phone1', 'ref_name2', 'ref_phone2',
                        'at1', 'at2', 'at3', 'at4', 'at5', 'as1', 'as2', 'as3', 'as4', 'as5']


def view_employee_list(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_A(request):
            database = employee_datatable()
            ginger = {
                'database': database,
            }
            return render(request, 'view_employees.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))

def view_employee_profile(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_A(request):
            database = employee_profile(kwargs['id'])
            ginger = {
                'database': database,
            }
            return render(request, 'employee_profile.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def form_employee(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_ho(request):
            if request.method == "POST":
                if all(item in request.POST and request.POST[item] != '' for item in employee_details):
                    if any(item in request.POST['job_profile'] for item in ['SM', 'RSO', 'ISO', 'IIC', 'IM', 'SC', 'MO', 'HK']):
                        return redirect(f"/./dashboard/hr-management/create-employee/{request.POST['name']}/{request.POST['age']}/{request.POST['address']}/{request.POST['phone']}/{request.POST['mail']}/{request.POST['ref_name1']}/{request.POST['ref_phone1']}/{request.POST['ref_name2']}/{request.POST['ref_phone2']}/{request.POST['at1']}/{request.POST['at2']}/{request.POST['at3']}/{request.POST['at4']}/{request.POST['at5']}/{request.POST['as1']}/{request.POST['as2']}/{request.POST['as3']}/{request.POST['as4']}/{request.POST['as5']}/{request.POST['job_profile']}/")
                    else:
                        ginger = {
                            'invalid_details': True,
                        }
                        return render(request, 'form_employee.html', ginger)
                else:
                    ginger = {
                        'invalid_details': True,
                    }
                    return render(request, 'form_employee.html', ginger)
            else:
                return render(request, 'form_employee.html')
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def add_employee(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_ho(request):
            if all(item in kwargs and item != '' for item in employee_details):
                create_employee_details = {
                    'status': 'ACTIVE',
                    'at1'   : kwargs['at1'],
                    'at2'   : kwargs['at2'],
                    'at3'   : kwargs['at3'],
                    'at4'   : kwargs['at4'],
                    'at5'   : kwargs['at5'],
                    'as1'   : kwargs['as1'],
                    'as2'   : kwargs['as2'],
                    'as3'   : kwargs['as3'],
                    'as4'   : kwargs['as4'],
                    'as5'   : kwargs['as5'],
                    'age'   : kwargs['age'],
                    'name'  : kwargs['name'],
                    'mail'  : kwargs['mail'],
                    'phone' : kwargs['phone'],
                    'address'    : kwargs['address'],
                    'ref_name1'  : kwargs['ref_name1'],
                    'ref_phone1' : kwargs['ref_phone1'],
                    'ref_name2'  : kwargs['ref_name2'],
                    'ref_phone2' : kwargs['ref_phone2'],
                    'job_profile': kwargs['job_profile'],
                    'creator' : get_cookie_user(request)
                }
                ##  CREATE EMPLOYEE FUNCTION  ##
                create_employee(create_employee_details)
                return redirect(reverse('homepage'))
            else:
                return redirect(reverse('form_employee'))
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


