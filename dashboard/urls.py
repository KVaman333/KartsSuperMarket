from django.urls import path
from .views      import *



urlpatterns = [
    path('goods-receipt/<str:po_num>/', good_receipt, name='gr'),
    path('update-goods-receipt/<str:po_num>/<str:invoice_amt>/<str:invoice_no>/<str:remark>/', update_gr, name='update_gr'),
    path('enter-po/', enter_po, name='po'),
]
