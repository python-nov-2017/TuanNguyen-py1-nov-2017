from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_lead$', views.add_lead, name="add_lead"),
    url(r'^get_leads/$', views.get_leads, name="get_leads"),    
]