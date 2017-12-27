# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.db.models import Count


from models import *
import bcrypt

# Create your views here.

def index(request):
    if 'id' in request.session:
        return redirect('/books')
    else:
        return render(request, 'book_review/index.html')

def registration_process(request):
    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            hash = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt())
            User.objects.create(name=request.POST['name'], alias=request.POST['alias'], email=request.POST['email'],password=hash)
            user = User.objects.get(email=request.POST['email'])
            if 'id' not in request.session:                 
                request.session['id'] = user.id  
                request.session['name'] = user.name
                request.session['alias'] = user.alias
            return redirect('/books')

def login_process(request):
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
                request.session['id'] = user.id
                request.session['name'] = user.name
                request.session['alias'] = user.alias
                return redirect('/books')       
    return HttpResponse("Login process")

def user_review(request):
    context = {
        'reviews': Review.objects.order_by("-created_at")[:3],
        'books':  Book.objects.annotate(review_count=Count('books')).filter(review_count__gte=1)
    }
    return render(request, 'book_review/user_review.html', context)

def logout_process(request):
    del request.session['id']
    return redirect('/')

def user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'books': Book.objects.filter(books__user__id=user_id),
    }
    return render(request, 'book_review/user.html', context)

def add_book(request):
    return render(request, 'book_review/add_book.html')

def add_book_process(request):
    if request.method == "POST":
        book = Book.objects.create(title=request.POST['title'], author=request.POST['author'])
        review = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=book, user=User.objects.get(id=request.session['id']))
    return redirect('/books')

def add_review_process(request, book_id):
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        review = Review.objects.create(review=request.POST['review'], rating=request.POST['rating'], book=book, user=User.objects.get(id=request.session['id']))
    return redirect('/books/{}'.format(book_id))

def book_review(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'reviews': Review.objects.filter(book__id=book_id).order_by("-created_at"),
    }
    return render(request, 'book_review/book_review.html', context)