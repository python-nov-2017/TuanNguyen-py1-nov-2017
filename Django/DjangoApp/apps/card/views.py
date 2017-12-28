# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.core import serializers
from models import *
# Create your views here.

def index(request):
    return render(request, "card/index.html")

def add(request):
    if len(request.POST['content']) > 0:
        Post.objects.create(content=request.POST['content'])
    return render(request, 'card/card.html', { 'cards': Post.objects.all() })