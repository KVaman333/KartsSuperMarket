from django.urls import path
from .views      import *



urlpatterns = [ # HEADER == dashboard/administrator/
    path('receipts/', view_receipt, name='view_receipt'),
    path('add-inventory/', add_inventory, name='add_inventory'),
    path('view-invoices/', view_invoice, name='view_invoices'),
]
