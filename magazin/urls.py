from django.conf.urls import url 
from magazin import views

ulrpatterns = [
     url(r'^$', views.index, name='index'),
    ]