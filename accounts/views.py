from django.core.files.storage import default_storage
from django.template.loader import get_template
from functions.accounts import add_pc, add_receipt_file, add_receipts, add_wo, get_receipt_id
from functions.authentication import validate_cookie, get_cookie_user, if_empty, get_time
from django.shortcuts import render, redirect, HttpResponse
from django.urls      import reverse

#  ACCOUNTS VIEWS  #

def wo_inventory(request, *args, **kwargs):
    if validate_cookie(request):
        if request.method == 'POST':
            if 'event' in request.POST and 'name' in request.POST and 'upc' in request.POST and 'size' in request.POST and 'quantity' in request.POST and 'prize' in request.POST and 'remarks' in request.POST:
                return redirect(f"/./dashboard/accounts/write-off-inventory/add/{request.POST['event']}/{request.POST['name']}/{request.POST['upc']}/{request.POST['size']}/{request.POST['quantity']}/{request.POST['prize']}/{request.POST['remarks']}/")
            else:
                ginger = {
                    'invalid_details':True,
                }
                return render(request, 'wo_inventory.html', ginger)
        else:
            return render(request, 'wo_inventory.html')
    else:
        return redirect(reverse('login'))


def receipt(request, *args, **kwargs):
    if validate_cookie(request):
        if request.method == 'POST':
            if 'name' in request.POST and 'amount' in request.POST and 'pay' in request.POST and 'remarks' in request.POST and 'file' in request.FILES:
                file = request.FILES['file']
                default_storage.save(file.name, file)
                return redirect(f"/./dashboard/accounts/receipts/add/{request.POST['name']}/{request.POST['amount']}/{request.POST['pay']}/{request.POST['remarks']}/{file.name}/")
            else:
                ginger = {
                    'invalid_details':True,
                }
                return render(request, 'receipt.html', ginger)
        else:
            return render(request, 'receipt.html')
    else:
        return redirect(reverse('login'))


def add_wo_inventory(request, *args, **kwargs):
    if validate_cookie(request):
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
        return redirect(reverse('login'))


def add_receipt(request, *args, **kwargs):
    if validate_cookie(request):
        user    = get_cookie_user(request)
        name    = kwargs['name']
        amount  = kwargs['amount']
        pay     = kwargs['pay']
        remarks = kwargs['remarks']
        file_name = kwargs['file_name']
        receipt_id = add_receipts(user,name,amount,pay,remarks,file_name)
        return redirect(f'/dashboard/accounts/receipt/confirm/{receipt_id}/')
    else:
        return redirect(reverse('login'))


def receipt_id_con(request, *args, **kwargs):
    if validate_cookie(request):
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
        return redirect(reverse('login'))


def petty_cash(request, *args, **kwargs):
    if validate_cookie(request):
        if request.method == 'POST':
            if all(item in request.POST for item in ['amount', 'account', 'to', 'by', 'remarks']):
                return redirect(f"/./dashboard/accounts/add-petty-cash/{request.POST['amount']}/{request.POST['account']}/{request.POST['to']}/{request.POST['by']}/{request.POST['remarks']}/")
            else:
                ginger = {
                    'invalid_datails': True,
                }
                return render(request, 'petty_cash.html', ginger)
        else:
            return render(request, 'petty_cash.html')
    else:
        return redirect(reverse('login'))

def add_petty_cash(request, *args, **kwargs):
    if validate_cookie(request):
        if 'HTTP_REFERER' in request.META and request.META['HTTP_REFERER'] == 'http://192.168.29.90:8000/dashboard/accounts/petty-cash/':
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
        return redirect(reverse('login'))

def petty_cash_pdf(request, *args, **kwargs):
    if validate_cookie(request):
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
        return redirect(reverse('login'))
