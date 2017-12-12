# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

inventory = []
item = {
    'id': 1,
    'name': "Dojo Tshirt",
    'price': 19.99
}
inventory.append(item)
item = {
    'id': 2,
    'name': "Dojo Sweater",
    'price': 29.99
}
inventory.append(item)
item = {
    'id': 3,
    'name': "Dojo Cup",
    'price': 4.99
}
inventory.append(item)
item = {
    'id': 4,
    'name': "Algorithm Book",
    'price': 49.99
}
inventory.append(item)

def index(request):
    request.session['inventory'] = inventory
    return render(request, "amadon/index.html")

def process(request):
    if request.method == "POST":
        if 'total' not in request.session:
            request.session['total'] = 0
        if 'count' not in request.session:
            request.session['count'] = 0            
        item_id = int(request.POST['id'])
        item_quantity = int(request.POST['quantity'])
        for item in inventory:
            if item['id'] == item_id:
                request.session['checkout'] = item['price'] * item_quantity
                request.session['total']+=request.session['checkout']
                request.session['count']+=item_quantity
    return redirect('amadon/checkout')

def checkout(request):
    return render(request, 'amadon/checkout.html')

def clear(request):
    request.session['total'] = 0
    request.session['count'] = 0
    return redirect('/amadon')