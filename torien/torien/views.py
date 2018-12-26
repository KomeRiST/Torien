from django.shortcuts import render_to_response, render
from . import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def login(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        err = 0
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, next)
                # Redirect to a success page.
            else:
                # Return a 'disabled account' error message
                err = 1
                return render(request, 'error/disabledaccount.html', {'form': form, 'err': err})
        else:
            # Return an 'invalid login' error message.
            err = 2
            return render(request, 'login.html', {'form': form, 'err': err})
    else:
        return render(request, 'login.html', {'form': form})


def index(request):
    return render_to_response('index.html')


def about(request):
    return render(request, 'index.html')


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
