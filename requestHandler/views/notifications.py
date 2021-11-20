from django.http.response import JsonResponse
from django.shortcuts import render, redirect



def update_notifications(request, *args, **kwargs):

    response = {
        'success': True
    }
    return JsonResponse(response)