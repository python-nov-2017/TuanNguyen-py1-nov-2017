# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import *
from django.contrib import messages
import bcrypt
# Create your views here.

def index(request):
    return render(request, "registration_login/index.html", {'users': User.objects.all() })

def success(request):
    return render(request,"registration_login/success.html")

def create(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            hash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password=hash)
            request.session['first_name'] = request.POST['first_name']
            return redirect('/success')

def login(request):
    if request.method == "POST":
        if len(User.objects.filter(email=request.POST['email'])) < 1:
            messages.error(request, "Email isn't exist.", extra_tags="email")
            return redirect('/')
        else:
            user = User.objects.filter(email=request.POST['email']).first()
            if not bcrypt.checkpw(request.POST['pw'].encode(),user.password.encode()):
                messages.error(request, "Wrong password", extra_tags='password')
                return redirect('/')
            else:
                request.session['email'] = request.POST['email']
                return redirect('/success')    

