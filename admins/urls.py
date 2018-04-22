from admins.views import index
from admins.views import create_page
from admins.views import get_page
from admins.views import customize_page
from django.conf.urls import url


urlpatterns = [
    url(r'^$', index, name='admin_index'),
    url(r'^customize_page/(?P<num>[0-9]+)/(?P<page_id>[0-9]+)$', customize_page, name='customize_page'),
    url(r'^get_page/(?P<num>[0-9]+)/$', get_page, name='get_page'),
    url(r'^create_page/(?P<num>[0-9]+)/$', create_page, name='create_page'),
]
