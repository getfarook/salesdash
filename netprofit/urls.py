"""netprofit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('admin/', admin.site.urls),
    # url(r"login/$", auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    url(r"login/$", auth_views.LoginView.as_view(),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"thanks/$", views.ThanksView.as_view(), name="thanks"),
    url(r"^sales/", include("sales.urls", namespace="sales")),
]

if settings.DEBUG:
    		import debug_toolbar
    		urlpatterns = [
        			url(r'^__debug__/',include(debug_toolbar.urls))
    		] + urlpatterns
