from functions.accounts import add_receipts, add_wo, get_receipt_id
from functions.authentication import validate_cookie, get_cookie_user
from django.shortcuts import render, redirect
from django.urls      import reverse

#  ACCOUNTS VIEWS  #

def wo_inventory(request, *args, **kwargs):
    if validate_cookie(request):
        if request.method == 'POST':
            if 'event' in request.POST and 'name' in request.POST and 'upc' in request.POST and 'size' in request.POST and 'quantity' in request.POST and 'prize' in request.POST and 'remarks' in request.POST:
                return redirect(f"/./dashboard/accounts/write-off-inventory/add/{request.POST['event']}/{request.POST['name']}/{request.POST['upc']}/{request.POST['size']}/{request.POST['quantity']}/{request.POST['prize']}/{request.POST['remarks']}/")
            else:
                print(request.POST)
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
            if 'name' in request.POST and 'amount' in request.POST and 'pay' in request.POST and 'remarks' in request.POST:
                return redirect(f"/./dashboard/accounts/receipts/add/{request.POST['name']}/{request.POST['amount']}/{request.POST['pay']}/{request.POST['remarks']}/")
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
        receipt_id = add_receipts(user,name,amount,pay,remarks)
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
