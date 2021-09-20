from functions.authentication import validate_cookie
from functions.tables         import stock_inventory
from django.shortcuts import render, redirect
from django.urls      import reverse


# Create your views here.


def inventory_table(request, *args, **kwargs):
    if validate_cookie(request):
        database = stock_inventory()
        ginger = {
            'admin_user': False,
            'database'  : database,
        }
        return render(request, 'inventory_table.html', ginger)
    else:
        return redirect(reverse('login'))
