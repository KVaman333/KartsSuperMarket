from django.urls import path
from .views      import *



urlpatterns = [
    path('write-off-inventory/', wo_inventory, name='wo'),
    path('receipt/',             receipt,      name='receipt'),
    path('receipt/confirm/<str:receipt_id>/', receipt_id_con, name='receipt'),
    path('write-off-inventory/add/<str:event>/<str:name>/<str:upc>/<str:size>/<str:quantity>/<str:prize>/<str:remarks>/', add_wo_inventory, name='add_wo'),
    path('receipts/add/<str:name>/<str:amount>/<str:pay>/<str:remarks>/<str:file_name>/', add_receipt, name='add_receipt'),
]
