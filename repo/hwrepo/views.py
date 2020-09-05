# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Leaseweb

from django.shortcuts import render


# Create your views here.

def main(request):
    items = Leaseweb.objects.all()
    assetsIds = []
    for server in items:
        assetsIds.append(str(server.assetId))

    html = '<br>'.join(assetsIds)
    return HttpResponse(html)
