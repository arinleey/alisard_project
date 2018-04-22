from django.db import models
from core.models_utils import pages_path
from core.models_utils import projects_path
from core.models_utils import services_path

# Create your models here.


class Pages(models.Model):
    header = models.CharField(max_length=512)
    body = models.TextField()
    PAGE_TYPE = (
        (0, 'Главная страница'),
        (1, 'О компании'),
        (2, 'Компания Алисард'),
        (3, 'Новости'),
        (4, 'Партнеры'),
        (5, 'Контакты'),
        (6, 'Проекты'),
        (12, 'Услуги'),
    )
    type = models.PositiveSmallIntegerField(default=0, choices=PAGE_TYPE)

    def __str__(self):
        return self.header


class MainPage(models.Model):
    # page = models.ForeignKey(Pages, related_name='main_page')
    name = models.CharField(max_length=30, unique=True, null=False)
    header_image = models.ImageField(upload_to=pages_path)
    header_text_ru = models.TextField(max_length=120)
    header_text_en = models.TextField(max_length=120)
    active = models.BooleanField(default=False)


class MainPageCarousel(models.Model):
    main_page = models.ForeignKey(MainPage, related_name='main_page_carousel')
    image = models.ImageField(upload_to=pages_path)
    text = models.TextField(max_length=120)


class MainPageIcons(models.Model):
    main_page = models.ForeignKey(MainPage, related_name='main_page_icons')
    icon = models.ImageField(upload_to=pages_path)
    icon_text_ru = models.TextField(max_length=70)
    icon_text_en = models.TextField(max_length=70)


class Projects(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to=projects_path)
    video = models.FileField(upload_to=projects_path)
    created_at = models.DateTimeField(auto_now=True)


class ProjectCategories(models.Model):
    project = models.ForeignKey(Projects, related_name='project_category')
    name = models.CharField(max_length=120, null=False, blank=False)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


class ProjectImages(models.Model):
    project = models.ForeignKey(Projects, related_name='project_images')
    image = models.ImageField(upload_to=projects_path, null=True, blank=True)


class Services(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to=services_path)
    video = models.FileField(upload_to=services_path)
    created_at = models.DateTimeField(auto_now=True)


class ServiceCategories(models.Model):
    service = models.ForeignKey(Services, related_name='service_category')
    name = models.CharField(max_length=120, null=False, blank=False)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


class ServiceImages(models.Model):
    service = models.ForeignKey(Services, related_name='service_images')
    image = models.ImageField(upload_to=services_path, null=True, blank=True)


