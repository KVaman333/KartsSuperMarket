from django.contrib import admin
from django.urls    import path, include

urlpatterns = [
    path('', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('requestHandler/', include('requestHandler.urls')),
]



handler404 = 'authentication.views.handler404'
handler500 = 'authentication.views.handler500'
