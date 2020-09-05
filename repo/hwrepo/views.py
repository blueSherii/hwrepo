# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Leaseweb

from django.shortcuts import render


# Create your views here.

def main(request):
    servers = Leaseweb.objects.all()
    return render(request, 'index.html', {'servers': servers})
