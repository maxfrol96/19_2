from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Наименование')
    product_desc = models.TextField(verbose_name='Описание', blank=True, null=True)
    product_img = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', blank=True, null=True)
    product_category = models.CharField(max_length=50, verbose_name='Категория')
    product_price = models.FloatField(verbose_name='Цена')
    product_create_date = models.DateField(verbose_name='Дата создания', blank=True, null=True)
    product_last_change_date = models.DateField(verbose_name='Дата последнего изменения', blank=True, null=True)

    def __str__(self):
        return f'{self.product_name} {self.product_category} {self.product_price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'




class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Наименование')
    category_desc = models.TextField(verbose_name='Описание', blank=True, null=True)
    # category_created_at = models.DateField(verbose_name='Создана')

    def __str__(self):
        return f'{self.category_name} {self.category_desc}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


