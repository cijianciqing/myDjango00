"""myDjango00 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path,include,re_path
from django.conf import settings
from django.views import static
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.views.static import serve

urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    # re_path(r'^media/(?P<path>.*)$', login_required(serve), kwargs={'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', login_required(serve), kwargs={'document_root': settings.STATIC_ROOT}, name='static'),
    # 注意login_required(serve)，日后需要权限控制
    re_path(r'^media/(?P<path>.*)$', static.serve, kwargs={'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', static.serve, kwargs={'document_root': settings.STATIC_ROOT},name='static'),
    # url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    # path('media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path('admin/|', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('admin/', admin.site.urls),
    path('app01/',include('app01.urls')),
    path('app02/',include('app02.urls')),
    path('app03/', include('app03.urls')),
]

