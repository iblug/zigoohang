"""planethelper URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as views_ckeditor
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="main"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
    path('posts/', include('posts.urls')),
    path('stores/', include('stores.urls')),
    path('carts/', include('carts.urls')),
    path('secondhands/', include('secondhands.urls')),
    path('chat/', include('chat.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path(r'^upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    # path(r'^browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
    path('upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path('browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
