from django.urls import path, include
from .views      import *



urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('notice/', notice, name='notice'),
    path('accounts/',include('accounts.urls')),
    path('administrator/',include('administrator.urls')),
    path('data-tables/',include('tables.urls')),
    path('goods-receipt/<str:po_num>/', good_receipt, name='gr'),
    path('update-goods-receipt/<str:po_num>/<str:invoice_amt>/<str:invoice_no>/<str:remark>/<str:file>/<str:user>/', update_gr, name='update_gr'),
    path('enter-po/', enter_po, name='po'),
]
