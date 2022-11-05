from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_quill.fields import QuillField


class Article(models.Model):

    title = models.CharField("Заголовок", max_length=1000, blank=True, null=True)
    slug = models.SlugField("Slug", null=False, blank=False, unique=True)
    content = QuillField("Содержание", null=True)
    status = models.CharField("Статус", max_length=20, default="Опубликовано")
    published = models.DateTimeField("Дата публикации", default=timezone.now, blank=True, null=True)
    video = models.CharField("Ссылка на видео", max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to='articles', blank=True)
    meta_keywords = models.CharField(verbose_name="Meta keywords", max_length=200, blank=True, null=True)
    meta_description = models.CharField('Meta description', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs=dict(slug=self.slug))

