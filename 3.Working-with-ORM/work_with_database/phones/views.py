from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    """
    Отображает каталог телефонов с возможностью сортировки.

    Представление получает список всех объектов Phone и при необходимости
    сортирует их в зависимости от параметра GET-запроса 'sort':

    - 'name' — сортировка по имени (по возрастанию)
    - 'min_price' — сортировка по цене (по возрастанию)
    - 'max_price' — сортировка по цене (по убыванию)
    """
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    """
    Отображает страницу с подробной информацией о товаре (телефоне).

    Получает объект Phone по его slug. Если объект не найден,
    возвращает 404 ошибку.
    Передаёт найденный объект в шаблон product.html для отображения.
    """
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone, }
    return render(request, template, context)
