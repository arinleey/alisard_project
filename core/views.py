from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


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