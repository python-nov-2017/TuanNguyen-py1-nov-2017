# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    if request.method == "POST":
        if 'counter' not in request.session:
            request.session['counter'] = 0
        request.session['counter']+=1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        redirect('/')

def result(request):
    return render(request, 'surveys/result.html')
