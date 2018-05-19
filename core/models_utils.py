from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import requests


def pages_path(instance, filename):
    return 'pages/%s/%s' % (instance.template_name, filename)


def projects_path(instance, filename):
    return 'projects/%s/%s' % (instance, filename)


def services_path(instance, filename):
    return 'services/%s/%s' % (instance, filename)
