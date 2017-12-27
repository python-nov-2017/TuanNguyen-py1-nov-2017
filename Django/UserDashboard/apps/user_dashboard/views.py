# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

import bcrypt
# Create your views here.

def index(request):
    return render(request, "user_dashboard/index.html")

def signin(request):
    if 'id' in request.session:
        return redirect('/dashboard')
    else:
        return render(request, 'user_dashboard/signin.html')


def login(request):
    if request.method == "POST":
        if len(User.objects.filter(email=request.POST['email'])) < 1:
            messages.error(request, "Email isn't exist.", extra_tags="email")
            return redirect('/signin')
        else:
            user = User.objects.filter(email=request.POST['email']).first()
            if not bcrypt.checkpw(request.POST['pw'].encode(),user.password.encode()):
                messages.error(request, "Wrong password", extra_tags='password')
                return redirect('/signin')
            else:
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name                
                request.session['user_level'] = user.user_level
                return redirect('/dashboard')   

def register(request):
    return render(request, 'user_dashboard/register.html')

def new(request):
    return render(request, 'user_dashboard/new.html')

def create(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            if request.session['id']:
                return redirect('users/new')
            else:
                return redirect('/register')
        else:
            hash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password=hash)
            user = User.objects.get(email=request.POST['email'])
            if user.id == 1:
                user.user_level = 'admin'
            else:
                user.user_level = 'normal'
            user.save()
            if not request.session['id']:                 
                request.session['id'] = user.id
                request.session['first_name'] = user.first_name
                request.session['user_level'] = user.user_level            
            return redirect('/dashboard')

def dashboard(request):
    u = User.objects.get(id=request.session['id'])
    context = {
        'one': u,
        'users': User.objects.all()
    }
    if u.user_level == 'admin':
        return render(request, 'user_dashboard/dashboard_admin.html', context)
    else:        
        return render(request, 'user_dashboard/dashboard.html', context)

def logout(request):
    del request.session['id']
    return redirect('/')

def destroy(request, user_id):
    u = User.objects.get(id=user_id)
    u.delete()
    return redirect('/dashboard')

def profile(request):
    return render(request, 'user_dashboard/profile.html', {'user': User.objects.get(id=request.session['id']) })

def edit(request):
    if request.method == "POST":
        user = User.objects.get(id = request.session['id'])
        print request.POST
        if 'pw' in request.POST and 'pw_confirm' in request.POST:
            if request.POST['pw'] != request.POST['pw_confirm']:
                messages.error(request, "Passwords don't match.", extra_tags="password")
            else:
                user.password = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
                messages.info(request, "Password updated", extra_tags="password")
        if set(['first_name', 'last_name', 'email']).issubset(request.POST):
            user.first_name = request.POST['first_name']       
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            messages.info(request, "Profile updated", extra_tags="profile")
        if 'desc' in request.POST:
            user.desc = request.POST['desc']
            messages.info(request, "Description updated", extra_tags="description")
        user.save()       
    return redirect('/users/profile')
 
def edit_process_user(request,user_id):
    if request.method == "POST":
        user = User.objects.get(id = user_id)
        print request.POST
        if 'pw' in request.POST and 'pw_confirm' in request.POST:
            if request.POST['pw'] != request.POST['pw_confirm']:
                messages.error(request, "Passwords don't match.", extra_tags="password")
            else:
                user.password = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
                messages.info(request, "Password updated", extra_tags="password")
        if set(['first_name', 'last_name', 'email']).issubset(request.POST):
            user.first_name = request.POST['first_name']       
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.user_level = request.POST['user_level']
            messages.info(request, "Profile updated", extra_tags="profile")
                    
        user.save()       
    return redirect('/users/edit/{}'.format(user.id))

def edit_user(request, user_id):
    return render(request, 'user_dashboard/profile_admin.html', {'user': User.objects.get(id=user_id) })

def show(request, user_id):
    return render(request, "user_dashboard/show.html", { "user": User.objects.get(id=user_id) })