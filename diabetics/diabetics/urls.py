"""diabetics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import path,include
from .import views
from django.views.generic import TemplateView
from django.conf.urls import url, include
from allauth.account.views import ConfirmEmailView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
   
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('rest-auth/password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name='password_reset_confirm'),
     path(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
     path(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
     path(r'^registration/complete/$', views.complete_view, name='account_confirm_complete'),
     path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.null_view, name='password_reset_confirm'),
     path(r'^rest-auth/facebook/', views.FacebookLogin.as_view(), name='fb_login')
     
]



