from django.core.management import BaseCommand
from catalog.models import Category

class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'category_name': 'TV', 'category_desc': 'LG'},
            {'category_name': 'TV', 'category_desc': 'Samsung'},
            {'category_name': 'Phone', 'category_desc': 'Apple'},
            {'category_name': 'Phone', 'category_desc': 'Samsung'},
        ]
        category_objects = []

        for category_item in category_list:
            category_objects.append(Category(**category_item))

        Category.objects.bulk_delete()
        Category.objects.bulk_create(category_objects)