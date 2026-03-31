import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    """
    Redirects user from the root URL to the bus stations page

    Используется как точка входа:
    при заходе на главную страницу происходит редирект
    на страницу со списком остановок.
    """
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    """
    Отображает список автобусных остановок с пагинацией.

    Логика работы:
    1. Читает CSV-file с остановками.
    2. Преобразует его в список словарей.
    3. Создает пагинатор (по 10 записей на странице).
    4. Получает текущую страницу из GET-параметра (?page=).
    5. Передает данные в шаблон.

    Важно:
    - CSV читает при каждом запросе.
    - Paginator.get_page() безопасно обрабатывает:
        * невалидные значения (например ?page=abs)
        * выход за границы страницы
    """

    # открываем CSV-file с кодировкой UTF-8
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as f:
        # DictReader превращает каждую строку CSV в словарь:
        # { 'Name': '...', 'Street': '...' }
        bus_stations_list = list(csv.DictReader(f))

    # создаём пагинатор:
    # первый аргумент — список данных
    # второй — количество элементов на страницу
    paginator = Paginator(bus_stations_list, 10)

    # получаем номер страницы из URL:
    # example: /stations/?page=2
    # если параметра нет → будет первая страница
    page_number = request.GET.get('page')

    # получаем объект страницы:
    # get_page сам обрабатывает ошибки (не число, слишком большое значение и т.д.)
    page = paginator.get_page(page_number)

    # передаем данные в шаблон
    context = {
        # список обьектов только для текущей страницы
        'bus_stations': page.object_list,

        # сам обьект страницы(нужен для навигации nex/prev)
        'page': page,
    }

    # рендерим HTML-шаблон с данными
    return render(request, 'stations/index.html', context)
