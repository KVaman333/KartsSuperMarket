from django.urls import path
from .views      import *



urlpatterns = [ #  HEADER == dashboard/data-tables/
    path('faq/', faq, name="faq"),
    path('inventory/', inventory_table, name="inventory_table"),
    path('departments/', class_table, name="classes"),
]
