"""zayavka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url

import dairy
import magazin
import moderator
import mounter
import payment
import registr
import registration
import service
import specialist

urlpatterns = [
    url(r'^$', registration.views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^dairy/', include('dairy.urls')),
    url(r'^magazin/', include('magazin.urls')),
    url(r'^moderator/', include('moderator.urls')),
    url(r'^mounter/', include('mounter.urls')),
    url(r'^payment/', include('payment.urls')),
    url(r'^registr/', include('registr.urls')),
    url(r'^registration/', include('registration.urls')),
    url(r'^service/', include('service.urls')),
    url(r'^specialist/', include('specialist.urls')),
]
