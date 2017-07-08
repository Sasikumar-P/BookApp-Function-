"""Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from TextBook import views 

urlpatterns = [
  url(r'^$', views.book_list, name='book_list'),
  url(r'^new$', views.book_create, name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', views.book_update, name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.book_delete, name='book_delete'),
]
