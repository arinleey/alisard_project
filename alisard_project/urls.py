"""alisard_project URL Configuration

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
from admins import urls as admins_urls
from django.conf.urls import url, include
from django.contrib import admin
from core import urls as core_urls
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog
from django.views.static import serve
from django.conf import settings
import notifications.urls
import os

urlpatterns = [
    url(r'^base_admin/', admin.site.urls),
    url(r'^admin/', include(admins_urls)),
    url(r'^', include(core_urls)),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]

#
urlpatterns += [ url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, }), url(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }), ]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=os.path.join(settings.MEDIA_ROOT, ''))
