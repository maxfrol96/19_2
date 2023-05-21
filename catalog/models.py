from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование')
    product_desc = models.TextField(verbose_name='Описание', blank=True, null=True)
    product_img = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', blank=True, null=True)
    product_category = models.CharField(max_length=50, verbose_name='Категория')
    product_price = models.FloatField(verbose_name='Цена')
    product_create_date = models.DateField(verbose_name='Дата создания', blank=True, null=True)
    product_last_change_date = models.DateField(verbose_name='Дата последнего изменения', blank=True, null=True)


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование')
    category_desc = models.TextField(verbose_name='Описание', blank=True, null=True)
    # category_created_at = models.DateField(verbose_name='Создана')


