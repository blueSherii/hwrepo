# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Leaseweb

from django.shortcuts import render


# Create your views here.

def main(request):
    return render(request, 'index.html')


def search(request):
    search_val = request.POST['search']
    servers = Leaseweb.objects.all()
    filtered = []
    for server in servers:
        if str(server.assetId) == search_val or server.serialNumber == search_val:
            filtered.append(server)
    return render(request, 'dev/search.dev.html', {'servers': filtered})
