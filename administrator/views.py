from functions.administrator import get_invoices, get_receipts
from functions.authentication import validate_cookie, validate_admin
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def view_receipt(request, *args, **kwargs):
    if validate_cookie(request):
        if validate_admin(request):
            database = get_receipts()
            ginger = {
                'admin_user': True,
                'database'  : database,
            }
            return render(request, 'view_receipts.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))


def view_invoice(request, *args, **kwargs):
    if validate_cookie(request):
        if validate_admin(request):
            database = get_invoices()
            ginger = {
                'admin_user': True,
                'database'  : database,
            }
            return render(request, 'view_receipts.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))
