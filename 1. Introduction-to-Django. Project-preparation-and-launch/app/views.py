import os
import zoneinfo
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse
from django.utils import timezone


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    # 1 вариант
    t_zone = zoneinfo.ZoneInfo('Europe/Moscow')
    current_time = timezone.localtime(timezone.now(), t_zone)
    msg = f'Текущее время: {current_time.strftime('%H:%M:%S')}'
    # 2 вариант
    current_time = datetime.now()
    msg = f'<h1>Текущее время: {current_time.strftime('%H:%M:%S')}</h1>'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    list_files = os.listdir(path='.')
    directory = '<br>'.join(list_files)
    msg = f'<h1>Рабочая директория:</h1>{directory}'
    return HttpResponse(msg)
    # raise NotImplemented
