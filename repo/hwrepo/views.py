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
    search_val = request.GET['search']
    print "Search term: " + search_val
    servers = Leaseweb.objects.all()
    filtered = []
    for server in servers:
        if search_val in str(server.assetId) or search_val in server.serialNumber:
            filtered.append(server)

    print len(filtered)
    return render(request, 'dev/search.dev.html', {'servers': filtered})
