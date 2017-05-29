"""geoportal URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/profile/$', include('main.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', views.home,name='home' ),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^data/',views.data, name='data'),
    url(r'^shamba/register/',views.registershamba, name='registershamba'),
    url(r'^shamba/discard/',views.discardshamba,name='discardshamba'),
    url(r'^shamba/changeowner/',views.changeowner,name='changeowner'),
    url(r'^statistics/',views.statistics,name='statistics'),
]
