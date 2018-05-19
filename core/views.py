from django.shortcuts import render
from core.models import MainPage

# Create your views here.


def main_page(request):
    page = MainPage.objects.first()
    return render(request, 'main_page.html', {'page': page})


def test_index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def news(request):
    return render(request, 'news.html')


def news_about(request):
    return render(request, 'news_about.html')


def contacts(request):
    return render(request, 'contacts.html')


def project(request):
    return render(request, 'project.html')


def services(request):
    return render(request, 'services.html')


def construction_kdk(request):
    return render(request, 'construction_kdk.html')


def industrial_facilities(request):
    return render(request, 'industrial_facilities.html')
