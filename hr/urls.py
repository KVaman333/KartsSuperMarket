from django.urls import path, include
from .views      import *

urlpatterns = [ #  HEADER == dashboard/hr-management/
    path('add-employee/', form_employee, name="form_employee"),
    path('view-employee/', view_employee_list, name="employee_list"),
    path('view-employee/<str:id>/', view_employee_profile, name="employee_profile"),
    path('create-employee/<str:name>/<str:age>/<str:address>/<str:phone>/<str:mail>/<str:ref_name1>/<str:ref_phone1>/<str:ref_name2>/<str:ref_phone2>/<str:at1>/<str:at2>/<str:at3>/<str:at4>/<str:at5>/<str:as1>/<str:as2>/<str:as3>/<str:as4>/<str:as5>/<str:job_profile>/', add_employee, name="add_employee"),
]
