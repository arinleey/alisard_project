from admins.views import index
from django.conf.urls import url


urlpatterns = [
    url(r'^$', index, name='admin_index'),
]
