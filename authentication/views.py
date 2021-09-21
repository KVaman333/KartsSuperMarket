from functions.authentication import change, get_cookie_user, user_auth, validate_cookie
from django.shortcuts         import render, redirect
from django.urls              import reverse
from django.template    import RequestContext

# Create your views here.

def domain(request, *args, **kwargs):
    return redirect(reverse('login'))


def login(request, *args, **kwargs):
    if validate_cookie(request):
        return redirect(reverse('homepage'))
    else:
        if request.method == 'POST':
            if 'username' in request.POST and 'password' in request.POST:
                verified = user_auth(request.POST['username'], request.POST['password'])
                if verified:
                    response = redirect(reverse('homepage'))
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


def change_password(request, *args, **kwargs):
    if validate_cookie(request):
        if request.method == 'POST':
            if 'old' in request.POST and 'new' in request.POST and 'con' in request.POST:
                old    = request.POST['old']
                new    = request.POST['new']
                con    = request.POST['con']
                cookie = get_cookie_user(request)
                verified = user_auth(cookie, old)
                if verified:
                    if new == con:
                        change(cookie, new)
                        return redirect(reverse('logout'))
                    else:
                        ginger = {
                            'invalid_old': False,
                            'invalid_con': True,
                            'incomplete' : False,
                        }
                        return render(request, 'change-password.html', ginger)
                else:
                    ginger = {
                        'invalid_old': True,
                        'invalid_con': False,
                        'incomplete' : False,
                    }
                    return render(request, 'change-password.html', ginger)
            else:
                ginger = {
                    'invalid_old': False,
                    'invalid_con': False,
                    'incomplete' : True,
                }
                return render(request, 'change-password.html', ginger)
        else:
            ginger = {
                'invalid_old': False,
                'invalid_con': False,
                'incomplete' : False,
            }
            return render(request, 'change-password.html', ginger)
    else:
        return redirect(reverse('login'))









def handler404(request, *args, **argv):
    if validate_cookie(request):
        response = redirect(reverse('pnf_dh'))
        return response
    else:
        response = redirect(reverse('pnf'))
        return response
def handler500(request, *args, **argv):
    if validate_cookie(request):
        response = redirect(reverse('se_dh'))
        return response
    else:
        response = redirect(reverse('se'))
        return response
def error404_handler(request, *args, **kwargs):
    return render(request, '404.html')
def error500_handler(request, *args, **kwargs):
    return render(request, '500.html')


