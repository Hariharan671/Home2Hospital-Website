"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from cnproject import views

func=views.A();

urlpatterns = [
    url(r'^$',views.home,name="home"),
    url('admin/', admin.site.urls),
    url(r'^logpage/$',func.index,name="index"),
    url(r'^info/$',views.information,name="info"),
    url(r'^login/$',func.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    url(r'^facilities/$',func.facilities,name="facilities"),
    url(r'^staff/$',func.staff,name="staff"),
    url(r'^tracker/$',views.tracker,name="tracker"),
    url(r'^medicoassistance/$',views.doubt,name="doubt"),
    url(r'^queries/$',views.lead,name="lead"),
    url(r'^donate/$',views.donate,name="donate"),
]
