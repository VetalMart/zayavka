from django.conf.urls import url 
from moderator import views

ulrpatterns = [
     url(r'^$', views.index, name='index'),
    ]