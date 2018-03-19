from django.shortcuts import render

# Create your views here.


def main_page(request):
    return render(request, 'main_page.html')


def test_index(request):
    return render(request, 'index.html')
