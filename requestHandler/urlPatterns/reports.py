from ..views.reports.scHandler import *
from django.urls import path


urlpatterns = [ #  HEADER == requestHandler/reports/
    path('scHandler/', getEditReport, name='scAjaxEditRequest'),
]