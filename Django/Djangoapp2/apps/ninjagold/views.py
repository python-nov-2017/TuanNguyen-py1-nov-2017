# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime

# Create your views here.

def index(request):
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
        request.session['record'] = []    
    return render(request,'ninjagold/index.html')

def process(request,building):
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
        request.session['record'] = []    
   
    if request.method == "POST":
        if building == 'farm':
            amount = random.randrange(10, 20)    
        elif building == 'cave':
            amount = random.randrange(5, 10) 
        elif building == 'house':
            amount = random.randrange(2, 5) 
        elif building == 'casino':
            amount = random.randrange(-50, 50)
        else:
            return redirect('/ninjagold')        
        request.session['current_gold']+=amount
        time = strftime("%Y/%m/%d %I:%M %p", gmtime())
        data = {
            'place': building,
            'gold': amount,
            'time': time
        } 
        saved_list = request.session.get('record', [])
        saved_list.insert(0,data)
        request.session['record'] = saved_list
    return redirect ('/ninjagold')

def reset(request):
    del request.session['current_gold']
    del request.session['record']
    return redirect('/ninjagold')