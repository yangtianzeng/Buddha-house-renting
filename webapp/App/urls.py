"""house URL Configuration

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
from App import views

urlpatterns = [
    url(r'^load_house/', views.load_house, name="load_house"),
    url(r'^load_house_before/', views.load_house_before, name="load_house_before"),
    url(r'^load_house_info/', views.load_house_info, name="load_house_info"),
    url(r'^add_like/', views.add_like, name="add_like"),
    url(r'^home/', views.home, name="home"),
    url(r'^load_city/', views.load_city, name="load_city"),

    url(r'^load_region/', views.load_region, name="load_region"),
    url(r'^load_user/', views.load_user, name="load_user"),

    url(r'^register/', views.register, name="register"),
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
    url(r'^blog/', views.blog, name="blog"),
    url(r'^test/', views.test, name="test"),
    url(r'^hello/', views.hello, name="hello"),
    url(r'^registerpage/', views.registerPage, name='registerpage'),
    url(r'^save_blog/',views.save_blog,name='save_blog'),


]
