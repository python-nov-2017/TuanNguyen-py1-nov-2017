# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    request.session['counter']+=1
    request.session['string'] = get_random_string(length=14)
    return render(request, "randomword/index.html")

def reset(request):
    request.session['counter'] = 0
    return redirect('/random_word')

def generate(request):
    if request.method == "POST":
        return redirect('/random_word')
    else:
        return redirect('/random_word')