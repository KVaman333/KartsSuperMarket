from functions.administrator import add_inventory_item, get_invoices, get_receipts, except_pack_upc
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


def add_inventory(request, *args, **kwargs):
    if validate_cookie(request):
        if validate_admin(request):
            if request.method == 'POST':
                if all(item in request.POST for item in ['stock_locator', 'item_order', 'description', 'sub_description', 'vendor_id', 'unit_upc', 'pack_upc', 'buy', 'sell', 'qty', 'department']):
                    if except_pack_upc(request):
                        stock_locator, item_order, description, sub_description, vendor_id, unit_upc, pack_upc, buy, sell, qty, department = request.POST['stock_locator'], request.POST['item_order'], request.POST['description'], request.POST['sub_description'], request.POST['vendor_id'], request.POST['unit_upc'], request.POST['pack_upc'], request.POST['buy'], request.POST['sell'], request.POST['qty'], request.POST['department']
                        if add_inventory_item(stock_locator, item_order, description, sub_description, vendor_id, unit_upc, pack_upc, buy, sell, qty, department):
                            return redirect(reverse('add_inventory'))
                        else:
                            ginger ={
                                'invalid_locator': True,
                                'stock_locator'  : stock_locator,
                                'item_order'     : item_order,
                                'description'    : description,
                                'sub_description': sub_description,
                                'vendor_id'      : vendor_id,
                                'unit_upc'       : unit_upc,
                                'pack_upc'       : pack_upc,
                                'buy'            : buy,
                                'sell'           : sell,
                                'qty'            : qty,
                                'department'     : department,
                            }
                            return render(request, 'add_inventory.html', ginger)
                    else:
                        stock_locator, item_order, description, sub_description, vendor_id, unit_upc, pack_upc, buy, sell, qty, department = request.POST['stock_locator'], request.POST['item_order'], request.POST['description'], request.POST['sub_description'], request.POST['vendor_id'], request.POST['unit_upc'], request.POST['pack_upc'], request.POST['buy'], request.POST['sell'], request.POST['qty'], request.POST['department']
                        ginger ={
                            'invalid_details': True,
                            'stock_locator'  : stock_locator,
                            'item_order'     : item_order,
                            'description'    : description,
                            'sub_description': sub_description,
                            'vendor_id'      : vendor_id,
                            'unit_upc'       : unit_upc,
                            'pack_upc'       : pack_upc,
                            'buy'            : buy,
                            'sell'           : sell,
                            'qty'            : qty,
                            'department'     : department,
                        }
                        return render(request, 'add_inventory.html', ginger)
                else:
                    print('invalid_locator')
                    ginger ={
                        'invalid_details': True,
                    }
                    return render(request, 'add_inventory.html', ginger)
            else:
                if request.path in request.META['HTTP_REFERER']:
                    ginger ={
                        'correct_details': True,
                    }
                    return render(request, 'add_inventory.html', ginger)
                else:
                    ginger ={
                        'invalid_details': False,
                    }
                    return render(request, 'add_inventory.html', ginger)
        else:
            return redirect(reverse('homepage'))
    else:
        return redirect(reverse('login'))
