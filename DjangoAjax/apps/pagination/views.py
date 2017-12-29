# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from models import *
from forms import *

# Create your views here.
LEADS_PER_PAGE = 3

def index(request):
    return render(request, "pagination/index.html", { "form": AddUserForm() })

def add_lead(request):
    form = AddUserForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('/pagination')

def get_leads(request=None):
    leads = User.objects.all()
    if any(x in ['name','from_date','to_date'] for x in request.POST):
        if request.POST['name'] != "":
            leads = leads.filter(first_name__startswith=request.POST['name'])
        if request.POST['from_date'] != "":
            leads = leads.filter(created_at__gt=request.POST['from_date'])        
        if request.POST['to_date'] != "":
            leads = leads.filter(created_at__lt=request.POST['to_date'])
    p = Paginator(leads, LEADS_PER_PAGE)
    pages = range(p.num_pages)
    pages = [x+1 for x in pages]
    subset = p.page(request.POST['page'])
    leads = subset.object_list  
    return render(request, 'pagination/user_table.html', { "leads": leads, "pages":pages })