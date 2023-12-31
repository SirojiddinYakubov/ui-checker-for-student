"""
URL configuration for core project.

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
from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.conf.urls.static import static


def main_page(request):
    return render(request, "index.html")


def about_page(request):
    return render(request, "about.html")


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', main_page),
                  path('about/', about_page),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
