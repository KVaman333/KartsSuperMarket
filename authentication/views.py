from functions.authentication import user_auth, validate_cookie
from django.shortcuts         import render, redirect
from django.urls              import reverse

# Create your views here.

def domain(request, *args, **kwargs):
    return redirect(reverse('login'))


def login(request, *args, **kwargs):
    if validate_cookie(request):
        return redirect(reverse('gr'))
    else:
        if request.method == 'POST':
            if 'username' in request.POST and 'password' in request.POST:
                verified = user_auth(request.POST['username'], request.POST['password'])
                if verified:
                    response = redirect(reverse('po'))
                    response.set_cookie('user',request.POST['username'])
                    return response
                else:
                    ginger = {
                        'invalid_details': True,
                    }
                    return render(request, 'login.html', ginger)
            else:
                ginger = {
                    'invalid_details': True,
                }
                return render(request, 'login.html', ginger)
        else:
            ginger = {
                'invalid_details': False,
            }
            return render(request, 'login.html', ginger)

def logout(request, *args, **kwargs):
    response = redirect(reverse('login'))
    response.delete_cookie('user')
    return response

