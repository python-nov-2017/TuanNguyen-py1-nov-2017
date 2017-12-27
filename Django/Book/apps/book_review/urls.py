from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration_process$', views.registration_process),
    url(r'^login_process$', views.login_process),
    url(r'^logout$', views.logout_process),    
    url(r'^books$', views.user_review),
    url(r'^books/add$', views.add_book),
    url(r'^books/add_book_process$', views.add_book_process), 
    url(r'^books/add_review_process/(?P<book_id>\d+)$', views.add_review_process),     
    url(r'^books/(?P<book_id>\d+)$', views.book_review),         
    url(r'^users/(?P<user_id>\d+)$', views.user),
    
]
