import json

from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from . import models

def parallax(request):
    kolls = models.Collection.objects.all()[:2]
    katitem = models.KategoryThing.objects.all()
    res = {"kolls": kolls, 'katalog': katitem}
    return render(request, "parallax.html", res)

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
    return render(request, 'myroom.html', {'selectnavmenu': 'myroom'})


def logout(request):
    auth.logout(request)
    return render(request, 'index.html')


def index(request):
    kolls = models.Collection.objects.all()[:2]
    katitem = models.KategoryThing.objects.all()
    res = {"kolls": kolls, 'katalog': katitem}
    return render(request, 'index.html', res)


def katalog(request):
    katitem = models.KategoryThing.objects.all()
    res = {'katalog': katitem, 'selectnavmenu': 'katalog'}
    return render(request, 'katalog.html', res)


def about(request):
    return render(request, 'about.html', {'selectnavmenu': 'about'})


def contacts(request):
    return render(request, 'contacts.html', {'selectnavmenu': 'contacs'})


def kollections(request):
    kollects = models.Collection.objects.all()[:2]
    res = {'kollects': kollects, 'selectnavmenu': 'kollections'}
    return render(request, 'kollections.html', res)


def alltovar(request):
    cat = request.GET.get("category", "")
    alltovar = models.Thing.objects.filter(kategory__name=cat)
    res = {'alltovar': alltovar, 'selectnavmenu': 'alltovar'}
    return render(request, 'alltovar.html', res)


def thing(request, id):
    thing = models.Thing.objects.get(pk=id)
    res = {'thing': thing, 'selectnavmenu': 'thing'}
    return render(request, 'thing.html', res)


def kollection(request, id):
    kollect = models.Collection.objects.get(pk=id)
    res = {'kollect': kollect, 'selectnavmenu': 'kollection'}
    return render(request, 'kollection.html', res)


def allkategories(request):
    kats = models.KategoryThing.objects.all()
    res = {'kats': kats, 'selectnavmenu': 'allkategories'}
    return render(request, 'allkategories.html', res)


def kategory(request, id):
    kategory = models.KategoryThing.objects.get(pk=id)
    tovary = models.Thing.objects.filter(kategory=kategory)
    res = {'kategory': kategory, 'tovary': tovary, 'selectnavmenu': 'kategory'}
    return render(request, 'kategory.html', res)
