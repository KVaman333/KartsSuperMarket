from django.urls import path
from .views      import *



urlpatterns = [ #  HEADER == dashboard/data-tables/
    path('inventory/', inventory_table, name="inventory_table"),
]
