from functions.authentication import validate_cookie
from functions.tables         import classes, stock_inventory
from functions.permissions    import *
from django.shortcuts import render, redirect
from django.urls      import reverse


# Create your views here.

def inventory_table(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_inventory(request):
            database = stock_inventory()
            ginger = {
                'admin_user': False,
                'database'  : database,
            }
            return render(request, 'view_inventory.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))

def faq(request, *args, **kwargs):
    if validate_cookie(request):
        return render(request, 'sop.html')
    else:
        return redirect(reverse('login'))

def class_table(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_inventory(request):
            database = classes()
            ginger = {
                'admin_user': False,
                'database'  : database,
            }
            return render(request, 'view_classes.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))

def upc_lookup(request, *args, **kwargs):
    if validate_cookie(request):
        if allow_inventory(request):
            if request.method == 'POST':
                if 'upc' in request.POST:
                    return redirect(request.META['HTTP_REFERER'])
                else:
                    return redirect(request.META['HTTP_REFERER'])
            else:
                return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))
