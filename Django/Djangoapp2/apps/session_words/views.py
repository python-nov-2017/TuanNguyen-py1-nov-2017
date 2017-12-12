# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
# Create your views here.

def index(request):
    return render(request, "session_words/index.html")

def add(request):
    if request.method == "POST":       
        if 'counter' not in request.session:
            request.session['counter'] = 0
        if 'word' in request.POST:
            word = request.POST['word']
        else:
            redirect('/session_words')
        if 'color' in request.POST:
            color = request.POST['color']
        else:
            color = "Blue"
        if 'big_font' in request.POST:
            font = "200%"
        else:
            redirect('/session_words')
        final_word = {
            'word': word,
            'color': color,
            'font': font,
            'time': strftime('%I:%M:%S %p, %b %d, %Y', gmtime()) 
        }
        saved_list = request.session.get('saved', [])
        saved_list.append(final_word)
        request.session['saved'] = saved_list
        request.session['counter']+=1            
    return redirect('/session_words')

def clear(request):
    if request.method == "POST":
        request.session['counter'] = 0
        del request.session['saved']
    return redirect('/session_words')