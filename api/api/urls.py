"""api URL Configuration

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
from django.urls import path, re_path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Nigeria Covid-19 API')
api_doc = include_docs_urls(title='Nigeria Covid-19 API')

urlpatterns = [
    path('somenewurl/', admin.site.urls),
    path(r'api/docs/', schema_view),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    re_path(r'^', include('states.urls')),
    re_path(r'^', include('confirmed.urls')),
    re_path(r'^', include('daily.urls')),
    path(r'', api_doc),
]
