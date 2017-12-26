# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
 

from models import *
# Create your views here.

def index(request):
    c = Course.objects.first()
    print c.name
    return render(request, "courses/index.html", { "courses": Course.objects.all()} )

def create(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
            return redirect('/')

def destroy(request, course_id):
    return render(request, "courses/delete.html", { "course": Course.objects.get(id=course_id) })

def delete(request, course_id):
    c = Course.objects.get(id=course_id)
    c.delete()
    return redirect('/')
    