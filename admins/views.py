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