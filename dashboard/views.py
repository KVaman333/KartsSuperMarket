from django.core.files.storage import default_storage
from functions.authentication  import get_cookie_user, validate_cookie
from functions.dashboard       import editable_po, gr_get, update_goods_receipt
from django.shortcuts import redirect, render
from django.urls      import reverse

# Create your views here.

def homepage(request, *args, **kwargs):
    if validate_cookie(request):
        return render(request, 'homepage.html')
    else:
        return redirect(reverse('login'))

def enter_po(request, *args, **kwargs):
    if validate_cookie(request):
        if request.method == 'POST':
            if 'po_num' in request.POST:
                po_num = request.POST['po_num']
                if editable_po(po_num):
                    return redirect(f"/./dashboard/goods-receipt/{po_num}/")
                else:
                    ginger = {
                        'no_details': False,
                        'non_editable_po': True,
                    }
                    return render(request, 'enter_po.html', ginger)                    
            else:
                ginger = {
                    'no_details': True,
                }
                return render(request, 'enter_po.html', ginger)
        else:
            ginger = {
            }
            return render(request, 'enter_po.html', ginger)
    else:
        return redirect(reverse('login'))


def good_receipt(request, *args, **kwargs):
    if validate_cookie(request):
        if request.method == 'GET':
            if 'po_num' in kwargs:
                po_num = kwargs['po_num']

                valid, po_amount, vendor = gr_get(po_num)

                if editable_po(po_num):
                    ginger = {
                        'logged_in': True,
                        'po_num'   : po_num,
                        'po_amount': po_amount,
                        'vendor'   : vendor,
                    }
                    return render(request, 'goods_receipt.html', ginger)
                else:
                    return redirect(reverse('po'))
        else:
            if 'invoice_amt' in request.POST and 'invoice_no' in request.POST and 'remark' in request.POST and 'file' in request.FILES and 'invoice_amt' != '' and 'invoice_no' != '':

                invoice_amt = request.POST['invoice_amt']
                invoice_no  = request.POST['invoice_no']
                remark      = request.POST['remark']
                file        = request.FILES['file']
                user        = get_cookie_user(request)
                default_storage.save(file.name, file)
                po_num      = request.path
                po_num      = po_num.split('/')
                po_num      = po_num[-2]

                return redirect(f"/./dashboard/update-goods-receipt/{po_num}/{invoice_amt}/{invoice_no}/{remark}/{file.name}/{user}/")
            else:
                return redirect(request.path)
    else:
        return redirect(reverse('login'))


def update_gr(request, *args, **kwargs):
    if validate_cookie(request):
        if 'po_num' in kwargs and 'invoice_amt' in kwargs and 'invoice_no' in kwargs and 'remark' in kwargs and 'file' in kwargs:
            po_num      = kwargs['po_num']
            invoice_amt = kwargs['invoice_amt']
            invoice_no  = kwargs['invoice_no']
            file        = kwargs['file']
            user        = kwargs['user']
            remark      = kwargs['remark']
            if editable_po(po_num):
                update_goods_receipt(po_num, invoice_amt, invoice_no, remark, file, user)

            return redirect(reverse('po'))
        else:
            return redirect(reverse('po'))
    else:
        return redirect(reverse('login'))


def notice(request, *args, **kwargs):
    if validate_cookie(request):
        return render(request, 'notice.html')
    else:
        return redirect(reverse('login'))







def error404_handler(request, *args, **kwargs):
    return render(request, '404_dh.html')
def error500_handler(request, *args, **kwargs):
    return render(request, '500_dh.html')