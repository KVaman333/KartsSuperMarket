from ..views.scanCoordinator import form, create
from django.urls import path


urlpatterns = [ # dashboard/daily-reports/Scan-Coordinator/
    path('form/', form, name="scForm"),
    path('form/<str:error>/', form, name="scForm"),
    path('create/<str:invoiceId>/<str:noItem>/<str:breakage>/<str:damaged>/<str:shortage>/<str:remarks>/', create, name="scCreate"),
]
