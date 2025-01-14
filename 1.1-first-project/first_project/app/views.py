from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'
    # правильные адреса страниц, используя функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # здесь HTML шаблона нет,  возвращается текст
    current_time = datetime.datetime.now().time().strftime('%H-%M-%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
   # возвращает список файлов в рабочей директории
    workdir = os.listdir('.')
    return HttpResponse(workdir)
    # raise NotImplemented
