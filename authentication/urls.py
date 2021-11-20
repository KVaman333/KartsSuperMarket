from django.urls import path
from .views      import *



urlpatterns = [
    path('PAGE-NOT-FOUND/', error404_handler, name='pnf'),
    path('SERVER-ERROR/', error500_handler, name='se'),
    path('', domain, name='domain'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('change-password/', change_password, name='change'),
]
