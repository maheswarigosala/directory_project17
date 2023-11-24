"""
URL configuration for project17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forms/',forms,name='forms'),
    path('tables/',tables,name='tables'),
    path('groupselector/',groupselector,name='groupselector'),
    path('pseudoselector/',pseudoselector,name='pseudoselector'),
    path('idselector/',idselector,name='idselector'),
    path('classselector/',classselector,name='classselector'),
    path('adjacentselector/',adjacentselector,name='adjacentselector'),
    path('internalstyles/',internalstyles,name='internalstyles'),
    path('animation/',animation,name='animation'),
    path('image/',image,name='image'),
    path('externalstyle/',externalstyle,name='externalstyle'),
]
