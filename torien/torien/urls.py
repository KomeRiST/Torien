"""torien URL Configuration

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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # url('^', include('django.contrib.auth.urls')),
    path('', views.index),
                  path('', include('social_django.urls')),
                  path('login/', views.login),
                  path('myroom/', views.myroom),
                  path('logout/', views.logout),
                  path('contacts/', views.contacts),
                  path('katalog/', views.katalog),
                  path('kollections/', views.kollections),
                  path('kollection/<int:id>/', views.kollection),
                  path('alltovar/', views.alltovar),
                  path('allkategories/', views.allkategories),
                  path('kategory/<int:id>/', views.kategory),
                  path('about/', views.about),
                  path('parallax/', views.parallax),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
