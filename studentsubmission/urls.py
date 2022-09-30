"""studentsubmission URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from homepage import views
from homepage import views
from files.views import fileupload, upload
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.second_view, name='home'),
    path('second', views.homepage_view, name='second'),
    path('login', views.login_view, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('register', views.register, name='register'),
    path('index', views.index, name='index'),
    path('upload', upload, name='upload'),
    path('uploadfile', fileupload, name='uploadfile'),

]

if settings.DEBUG:
    urlpatterns == static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
