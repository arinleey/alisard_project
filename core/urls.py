"""alisard URL Configuration

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
from django.conf.urls import url
from core.views import contacts
from core.views import news
from core.views import news_about
from core.views import about
from core.views import main_page
from core.views import project
from core.views import services
from core.views import construction_kdk


urlpatterns = [
    url(r'^contacts/$', contacts, name="contacts"),
    url(r'^news_about/$', news_about, name="news_about"),
    url(r'^about/$', about, name="about"),
    url(r'^$', main_page, name="main_page"),
    url(r'^news/$', news, name="news"),
    url(r'^project/$', project, name="project"),
    url(r'^services/$', services, name="services"),
    url(r'^construction_kdk/$', construction_kdk, name="construction_kdk"),
]