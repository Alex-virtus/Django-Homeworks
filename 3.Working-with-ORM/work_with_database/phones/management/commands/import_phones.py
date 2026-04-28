import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    """
    Импортирует данные о телефонах из CSV-файла в базу данных.

    Читает файл 'phones.csv', создаёт или обновляет объекты Phone
    по полю id. При обновлении используются данные из CSV, а также
    генерируется slug из названия и преобразуется поле LTE в boolean.
    """
    help = 'Imports data from csv to the database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.update_or_create(
                id=phone['id'],
                defaults={
                    'name': phone['name'],
                    'price': phone['price'],
                    'image': phone['image'],
                    'release_date': phone['release_date'],
                    'lte_exists': phone['lte_exists'] == 'True',
                    'slug': slugify(phone['name']),
                }
            )
