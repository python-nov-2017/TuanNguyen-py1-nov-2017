# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from models import *
# Create your views here.

def index(request):
    return render(request, "users/index.html", {"users": User.objects.all()})

def new(request):
    return render(request, "users/register.html")

def create(request):    
    if request.method == "POST":
        User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
        print User.objects.first()
    return redirect('/users')

def edit(request, user_id):
    return render(request, "users/edit.html", {"user": User.objects.get(id=user_id)})

def update(request):
    if request.method =="POST":
        u = User.objects.get(id=request.POST["id"])
        u.first_name = request.POST["first_name"]
        u.last_name = request.POST["last_name"]
        u.email = request.POST["email"]
        u.save()
    return render(request, "users/show.html", { "user": User.objects.get(id=request.POST["id"]) })



def show(request, user_id):
    return render(request, "users/show.html", { "user": User.objects.get(id=user_id) })

def destroy(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('/dashboard')

