from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^login$', views.login),  
    url(r'^register$', views.register), 
    url(r'^users/new$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/profile$', views.profile),       
    url(r'^users/edit$', views.edit), 
    url(r'^users/edit/(?P<user_id>\d)$', views.edit_user),
    url(r'^users/edit_process/(?P<user_id>\d)$', views.edit_process_user),           
    url(r'^users/show/(?P<user_id>\d)$', views.show),               
    url(r'^create$', views.create), 
    url(r'^dashboard', views.dashboard),
    url(r'logout$', views.logout),
    url(r'(?P<user_id>\d)/destroy$', views.destroy),

]