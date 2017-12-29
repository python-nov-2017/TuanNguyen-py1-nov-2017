# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core import serializers
from models import *

# Create your views here.

def index(request):
    return render(request, 'note/index.html', { "notes": Note.objects.all() } )

def add(request):
    if 'title' in request.POST:
        if request.POST['title'] != "":
            Note.objects.create(title=request.POST['title'])        
    return render(request, 'note/note.html', { "notes": Note.objects.all() })

def add_content(request):
    print request.POST
    if request.POST['content'] != "":
        print request.POST['content']
        n = Note.objects.get(id=request.POST['id'])
        n.content = request.POST['content']
        n.save()      
    return render(request, 'note/note.html', { "notes": Note.objects.all() })

def delete(request):
    n = Note.objects.get(id=request.POST['id'])
    n.delete()
    return render(request, 'note/note.html', { "notes": Note.objects.all() })