from admins.utils import check_data
from core.models import MainPage
from core.models import MainPageIcons
from core.models import MainPageCarousel
from core.models import AboutCompanyPage
from core.models import AboutCompanyAdvantages
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.translation import ugettext_lazy as _

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
    print(num, '<<< NUM')
    page = None
    if num == 0:
        try:
            page = MainPage.objects.all()
        except MainPage.DoesNotExist as e:
            print(e, '<------- Main_page Exception')
    elif num == 1:
        try:
            page = AboutCompanyPage.objects.all()
        except Exception as e:
            print(e, '<------- AboutPage Exception')
    return render(
        request,
        'admins/pages/get_page.html',
        {
            'data': page,
            'num': num
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
    print(num, '<<<<< CREATE PAGE NUM')
    print(request.method, '<<<<< REQUEST METHOD')
    if request.method == 'POST':
        page = None
        data = request.POST
        print(data)
        print('=====================================================================')
        print(request.POST)
        print('=====================================================================')
        files = request.FILES
        error, key = check_data(request.POST)
        if error:
            return JsonResponse({'error': True, 'invalid_key': key})
        if num == '0':
            try:
                # page = MainPage.objects.filter().first()
                page = MainPage.objects.create(template_name=data.get('template_name'),
                                               header_image=files.get('header_image'),
                                               image_alt=data.get('image_alt'),
                                               header_text_ru=data.get('header_text_ru'),
                                               header_text_en=data.get('header_text_en'),
                                               active=False)
            except Exception as e:
                print(e, '<------- Main_page Exception')
                return JsonResponse({
                    'error': True,
                    'subject': _('Ошибка при создании {}!').format(data.get('template_name')),
                    'message': _('Ошибка при создании шаблона главной страницы, пожалуйста попробуйте снова.'),
                    'status': 2,
                })

            try:
                for key in files:
                    file = files.get(key)
                    data_key_en = data.get(key.split('_')[0] + '_text_' + key.split('_')[2] + '_en')
                    data_key_ru = data.get(key.split('_')[0] + '_text_' + key.split('_')[2] + '_ru')
                    image_alt_key = data.get(key + '_alt')
                    if key.split('_')[0] == 'icon':
                        MainPageIcons.objects.create(main_page=page, icon=file, icon_text_ru=data_key_ru,
                                                     icon_text_en=data_key_en, image_alt=image_alt_key)
                    elif key.split('_')[0] == 'slide':
                        MainPageCarousel.objects.create(main_page=page, image=file, slide_text_ru=data_key_ru,
                                                        slide_text_en=data_key_en, image_alt=image_alt_key)
            except Exception as e:
                print(e, '<------- Main Page Files exception')
                return JsonResponse({
                    'error': True,
                    'subject': _('Ошибка при создании {}!').format(data.get('template_name')),
                    'message': _('Ошибка при добавлении иконок, либо слайдов для главной страницы,'
                                 ' пожалуйста попробуйте снова.'),
                    'status': 2,
                })

            return JsonResponse({
                'error': False,
                'subject': _('Шаблон {} успешно создан!').format(data.get('template_name')),
                'message': _('Шаблон главной страницы успешно создан, но не активирован.'
                             'Через 3 секунды вы будете перенаправлены на страницу выбора шаблона.')
            })
    else:
        page_name = ''
        template_name= None
        if num == '0':
            page_name = _('Главная страница')
            template_name = 'main_page'
        if num == '1':
            page_name = _('Компания')
            template_name = 'about_company'
        return render(
            request,
            'admins/pages/create_page.html',
            {
                'page_name': page_name,
                'num': num,
                'template_name': template_name
            }
        )
