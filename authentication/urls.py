from django.urls import path
from .views      import *



urlpatterns = [
    path('', domain, name='domain'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
