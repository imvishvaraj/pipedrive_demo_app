"""cmsapp URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from dashbd.views import Home, Customer, hm, PipeDriveSettings
from accounts.views import Login, Logout, Register


urlpatterns = [
    path('', hm, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/register/', Register.as_view(), name='register'),
    path('accounts/logout/', Logout.as_view(), name='logout'),
    path('new_customer/', Customer.as_view(), name='customer'),
    path('settings/', PipeDriveSettings.as_view(), name='settings')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
