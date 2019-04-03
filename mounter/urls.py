from django.conf.urls import url 
from mounter import views

ulrpatterns = [
     url(r'^$', views.index, name='index'),
    ]