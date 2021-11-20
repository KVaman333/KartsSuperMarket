from django.urls import path, include
from .views.notifications import *


urlpatterns = [#  HEADER == requestHandler/
    path('notifications/', update_notifications),
    path('reports/', include('requestHandler.urlPatterns.reports')),
]
