from core.models import MainPage
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

login_url = "/base_admin/login/"


@login_required(login_url=login_url)
@user_passes_test(lambda u: u.is_superuser or u.is_seo_manager, login_url=login_url)
def index(request):
    return render(
        request,
        'admins/index.html',
        # 'admin_base.html',
    )


@login_required(login_url=login_url)
@user_passes_test(lambda u: u.is_superuser or u.is_seo_manager, login_url=login_url)
def get_page(request, num=None):
    print(num)
    page = None
    if num == 0:
        try:
            page = MainPage.objects.all()
        except MainPage.DoesNotExist as e:
            print(e, '<------- Main_page Exception')

    return render(
        request,
        'admins/pages/get_page.html',
        {
            'data': page
        }
    )


@login_required(login_url=login_url)
@user_passes_test(lambda u: u.is_superuser or u.is_seo_manager, login_url=login_url)
def customize_page(request, num=None, id=None):
    try:
        page = MainPage.objects.filter().first()
    except MainPage.DoesNotExist as e:
        page = ''
        print(e, '<------- Main_page Exception')
    return render(
        request,
        'admins/pages/customize_page.html',
        {
            'data': page
        }
        # 'admin_base.html',
    )


@login_required(login_url=login_url)
@user_passes_test(lambda u: u.is_superuser or u.is_seo_manager, login_url=login_url)
def create_page(request, num=None):
    try:
        page = MainPage.objects.filter().first()
    except MainPage.DoesNotExist as e:
        page = ''
        print(e, '<------- Main_page Exception')
    return render(
        request,
        'admins/pages/customize_page.html',
        {
            'data': page
        }
        # 'admin_base.html',
    )
