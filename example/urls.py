"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from example import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^digg_pagination_raw/$', views.DiggPaginationRawView.as_view(), name = 'digg_pagination_raw'),
    url(r'^digg_pagination_tables2/$', views.DiggPaginationTables2View.as_view(), name = 'digg_pagination_tables2'),
    url(r'^tables2/$', views.Tables2View.as_view(), name = 'tables2'),
]
