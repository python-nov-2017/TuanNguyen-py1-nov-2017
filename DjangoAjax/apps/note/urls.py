from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^add_content$', views.add_content),
    url(r'^delete$', views.delete),    
]