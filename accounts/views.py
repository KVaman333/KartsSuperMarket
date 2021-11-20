from django.core.files.storage import default_storage
from django.template.loader import get_template
from functions.accounts import add_pc, add_receipt_file, add_receipts, add_wo, get_receipt_id
from functions.authentication import validate_cookie, get_cookie_user, if_empty, get_time
from django.shortcuts import render, redirect, HttpResponse
from django.urls      import reverse
from functions.permissions import *

#  ACCOUNTS VIEWS  #

def wo_inventory(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_iwoff(request):
            if request.method == 'POST':
                if all(item in request.POST and request.POST[item] != '' for item in ['event', 'name', 'upc', 'size', 'quantity', 'price', 'remarks']):
                    if any(item in request.POST['event'] for item in ['Used', 'Expired', 'Breakage', 'Damaged', 'Missing', 'Tampered']):
                        return redirect(f"/./dashboard/accounts/write-off-inventory/add/{request.POST['event']}/{request.POST['name']}/{request.POST['upc']}/{request.POST['size']}/{request.POST['quantity']}/{request.POST['price']}/{request.POST['remarks']}/")
                    else:
                        ginger = {
                            'invalid_details':True,
                        }
                        return render(request, 'wo_inventory.html', ginger)
                else:
                    ginger = {
                        'invalid_details':True,
                    }
                    return render(request, 'wo_inventory.html', ginger)
            else:
                return render(request, 'wo_inventory.html')
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def receipt(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_receipts(request):
            if request.method == 'POST':
                if all(item in request.POST and request.POST[item] != '' for item in ['name', 'amount', 'pay', 'remarks']) and 'file' in request.FILES:
                    if any(item in request.POST['pay'] for item in ['Cash', 'Credit Card', 'Online Payment', 'Cheque']):
                        file = request.FILES['file']
                        default_storage.save(file.name, file)
                        return redirect(f"/./dashboard/accounts/receipts/add/{request.POST['name']}/{request.POST['amount']}/{request.POST['pay']}/{request.POST['remarks']}/{file.name}/")
                    else:
                        ginger = {
                            'invalid_details':True,
                        }
                        return render(request, 'receipt.html', ginger)
                else:
                    ginger = {
                        'invalid_details':True,
                    }
                    return render(request, 'receipt.html', ginger)
            else:
                return render(request, 'receipt.html')
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def add_wo_inventory(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_iwoff(request):
            user     = get_cookie_user(request)
            event    = kwargs['event']
            name     = kwargs['name']
            upc      = kwargs['upc']
            size     = kwargs['size']
            quantity = kwargs['quantity']
            prize    = kwargs['prize']
            remarks  = kwargs['remarks']
            add_wo(user,event,name,upc,size,quantity,prize,remarks)
            return redirect(reverse('wo'))
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def add_receipt(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_receipts(request):
            user    = get_cookie_user(request)
            name    = kwargs['name']
            amount  = kwargs['amount']
            pay     = kwargs['pay']
            remarks = kwargs['remarks']
            file_name = kwargs['file_name']
            receipt_id = add_receipts(user,name,amount,pay,remarks,file_name)
            return redirect(f'/dashboard/accounts/receipt/confirm/{receipt_id}/')
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def receipt_id_con(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_receipts(request):
            if request.method == 'POST':
                return redirect(reverse('receipt'))
            else:
                if 'receipt_id' in kwargs:
                    id = kwargs['receipt_id']
                    ginger={'id':id}
                    return render(request, 'receipt_id_confirm.html', ginger)
                else:
                    return redirect(reverse('receipt'))
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def petty_cash(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_pc(request):
            if request.method == 'POST':
                if all(item in request.POST and request.POST[item] != '' for item in ['amount', 'account', 'to', 'by', 'remarks']):
                    return redirect(f"/./dashboard/accounts/add-petty-cash/{request.POST['amount']}/{request.POST['account']}/{request.POST['to']}/{request.POST['by']}/{request.POST['remarks']}/")
                else:
                    ginger = {
                        'invalid_datails': True,
                    }
                    return render(request, 'petty_cash.html', ginger)
            else:
                return render(request, 'petty_cash.html')
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))

def add_petty_cash(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_pc(request):
            if 'HTTP_REFERER' in request.META and request.META['HTTP_REFERER'] == 'http://192.168.29.90:8000/dashboard/accounts/petty-cash/' or request.META['HTTP_REFERER'] == 'https://karts-supermarket.herokuapp.com/dashboard/accounts/petty-cash/'or request.META['HTTP_REFERER'] == 'http://karts-supermarket.herokuapp.com/dashboard/accounts/petty-cash/':
                amount  = kwargs['amount']
                account = kwargs['account']
                to      = kwargs['to']
                by      = kwargs['by']
                remarks = kwargs['remarks']
                user    = get_cookie_user(request)

                id = add_pc(amount, account, to, by, remarks, user)

                return redirect(f"/./dashboard/accounts/petty-cash-pdf/{id}/{amount}/{account}/{to}/{by}/")
            else:
                return redirect(reverse('petty_cash'))
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))

def petty_cash_pdf(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_pc(request):
            number      = kwargs['number']
            amount  = kwargs['amount']
            account = kwargs['account']
            to      = kwargs['to']
            by      = kwargs['by']

            ginger = {
                'amount' : amount,
                'account': account,
                'to'     : to,
                'by'     : by,
                'number' : number,
                'date'   : get_time('date')
            }
            return render(request, 'petty_cash_pdf.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))
