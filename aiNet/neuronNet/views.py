from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = NeuronNet.objects.all()
    return render(request, 'neuronNet/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'neuronNet/about.html', {'menu': menu, 'title': 'О сайте'})


def categories(request, netid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f'<h1>Разные нейросетевые модели</h1><p>{netid}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def pageNotFound(reqest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
