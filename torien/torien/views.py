import json

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from . import models


def login(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # if request.user.is_authenticated:
        #     print('logout...')
        #     auth.logout(request)
        user = auth.authenticate(username=username, password=password)
        print('user:', user)
        if user is not None:
            print('user: user is not None')
            if user.is_active:
                print('user: is_active')
                auth.login(request, user)
                err = 'ok'
                print('message: ', err)
                res = json.dumps({'message': err})
                return HttpResponse(res)
                # return render(request, 'index.html')
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                print('user: is NOT active')
                err = 'disabled account'
                print('message: ', err)
                res = json.dumps({'message': err})
                return HttpResponse(res)
        else:
            # Return an 'invalid login' error message.
            err = 'invalid login'
            print('message: ', err)
            res = json.dumps({'message': err})
            return HttpResponse(res)
    else:
        err = ''
        print('message: ', err)
        return render(request, 'login.html', {'form': form, 'message': err})


def myroom(request):
    return render(request, 'myroom.html')


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def katalog(request):
    return render(request, 'katalog.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def kollections(request):
    kollects = models.Collection.objects.all()[:2]
    res = {'kollects': kollects}
    return render(request, 'kollections.html', res)


def alltovar(request):
    alltovar = models.Thing.objects.all()
    res = {'alltovar': alltovar}
    return render(request, 'alltovar.html', res)


def thing(request, id):
    thing = models.Thing.objects.get(pk=id)
    res = {'thing': thing}
    return render(request, 'thing.html', res)


def kollection(request, id):
    kollect = models.Collection.objects.get(pk=id)
    res = {'kollect': kollect}
    return render(request, 'kollection.html', res)


def allkategories(request):
    kats = models.KategoryThing.objects.all()
    res = {'kats': kats}
    return render(request, 'allkategories.html', res)


def kategory(request, id):
    kategory = models.KategoryThing.objects.get(pk=id)
    tovary = models.Thing.objects.filter(kategory=kategory)
    res = {'kategory': kategory, 'tovary': tovary}
    return render(request, 'kategory.html', res)
