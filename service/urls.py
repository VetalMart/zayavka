from django.conf.urls import url 
from dairy import views

ulrpatterns = [
     url(r'^$', views.index, name='index'),
    ]