from django.urls import path
from .views      import *



urlpatterns = [ #  HEADER == dashboard/data-tables/
    path('faq/', faq, name="faq"),
    path('departments/', class_table, name="classes"),
    path('upc-lookup/', upc_lookup, name="upc_lookup"),
    path('inventory/', inventory_table, name="inventory_table"),
]
