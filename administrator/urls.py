from django.urls import path
from .views      import *



urlpatterns = [ # HEADER == dashboard/administrator/
    path('receipts/', view_receipt, name='view_receipt'),
    path('view-invoices/', view_invoice, name='view_invoices'),
    path('add-inventory/', add_inventory, name='add_inventory'),
    path('add-employee/', add_employee, name='add_employee'),
    path('form-notice/', form_notice, name='form_notice'),
    path('create-notice/<str:title>/<str:text>/', create_notice, name='create_notice'),
]
