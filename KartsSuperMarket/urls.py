from django.contrib import admin
from django.urls    import path, include

urlpatterns = [
    path('', include('authentication.urls')),
    path('dashboard/', include('dashboard.urls')),
]
