# Generated by Django 4.1.3 on 2023-05-21 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('category_desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('product_desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('product_img', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение(превью)')),
                ('product_category', models.CharField(max_length=50, verbose_name='Категория')),
                ('product_price', models.FloatField(verbose_name='Цена')),
                ('product_create_date', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('product_last_change_date', models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')),
            ],
        ),
    ]
