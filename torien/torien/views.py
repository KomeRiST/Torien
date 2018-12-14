from django.shortcuts import render_to_response, render
from . import models


def index(request):
    return render_to_response('index.html')


def about(request):
    return render(request, 'index.html')


def kollections(request):
    kollects = models.Collection.objects.all()[:2]
    res = {'kollects': kollects}
    return render(request, 'kollections.html', res)


def kollection(request, id):
    return render(request, 'kollection.html')
