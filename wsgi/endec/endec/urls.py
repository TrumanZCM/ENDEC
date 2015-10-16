"""endec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import os
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin
from tools.views import *
from django.views.generic import TemplateView

DJ_PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(DJ_PROJECT_DIR)
WSGI_DIR = os.path.dirname(BASE_DIR)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^urlendec/', URLEndecView.as_view(), name='urlendec'),
    url(r'^binendec/', BinEndecView.as_view(), name='binendec'),
    url(r'^octendec/', OctEndecView.as_view(), name='octendec'),
    url(r'^hexendec/', HexEndecView.as_view(), name='hexendec'),
    url(r'^b64endec/', B64EndecView.as_view(), name='b64endec'),
    url(r'^hashendec/', HashEndecView.as_view(), name='hashendec'),
    url(r'^cheatsheet/(?P<sheet_name>[a-z]+)/$', CSView.as_view(), name='cheatsheet'),
]

from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)