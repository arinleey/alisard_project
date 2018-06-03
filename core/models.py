from django.db import models
from core.models_utils import pages_path
from core.models_utils import projects_path
from core.models_utils import services_path

# Create your models here.


class BasePage(models.Model):
    template_name = models.CharField(max_length=30, unique=True, null=False)
    image = models.ImageField(upload_to=pages_path)
    header_text_ru = models.TextField(max_length=240)
    header_text_en = models.TextField(max_length=240)
    active = models.BooleanField(default=False)
    image_alt = models.CharField(max_length=30)

    class Meta:
        abstract = True


class MainPage(BasePage):
    pass
    # template_name = models.CharField(max_length=30, unique=True, null=False)
    # header_image = models.ImageField(upload_to=pages_path)
    # image_alt = models.CharField(max_length=30)
    # header_text_ru = models.TextField(max_length=240)
    # header_text_en = models.TextField(max_length=240)
    # active = models.BooleanField(default=False)


class MainPageCarousel(models.Model):
    main_page = models.ForeignKey(MainPage, related_name='main_page_carousel')
    image_alt = models.CharField(max_length=30)
    image = models.ImageField(upload_to=pages_path)
    slide_text_ru = models.TextField(max_length=240)
    slide_text_en = models.TextField(max_length=240)


class MainPageIcons(models.Model):
    main_page = models.ForeignKey(MainPage, related_name='main_page_icons')
    image = models.ImageField(upload_to=pages_path)
    image_alt = models.CharField(max_length=30)
    icon_text_ru = models.TextField(max_length=70)
    icon_text_en = models.TextField(max_length=70)


class AboutCompanyPage(BasePage):
    # template_name = models.CharField(max_length=30, unique=True, null=False)
    # header_image = models.ImageField(upload_to=pages_path)
    # image_alt = models.CharField(max_length=30)
    # header_text_ru = models.TextField(max_length=240)
    # header_text_en = models.TextField(max_length=240)
    # active = models.BooleanField(default=False)
    main_content_title_ru = models.TextField(max_length=60)
    main_content_title_en = models.TextField(max_length=60)
    main_content_text_ru = models.TextField(null=False)
    main_content_text_en = models.TextField(null=False)
    main_advantages_title_ru = models.TextField(max_length=60)
    main_advantages_title_en = models.TextField(max_length=60)


class AboutCompanyAdvantages(models.Model):
    about_company = models.ForeignKey(AboutCompanyPage, related_name='about_company_advantages')
    advantages_title_ru = models.TextField(max_length=30, null=False)
    advantages_title_en = models.TextField(max_length=30, null=False)
    advantages_content_text_ru = models.TextField(max_length=240, null=False)
    advantages_content_text_en = models.TextField(max_length=240, null=False)
    image = models.ImageField(upload_to=pages_path)
    image_alt = models.CharField(max_length=30)


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


