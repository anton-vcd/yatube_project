from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# Главная страница
def index(request):    
    return HttpResponse('Главная страница posts')


# Страница со списком group
def group_posts(request):
    return HttpResponse('список group_posts')


# Страница с информацией об одном конкретном;
# view-функция принимает параметр pk из path()
def group_posts_detail(request, pk):
    return HttpResponse(f'Group posts номер {pk}')

def group_posts_slug(request, pk):
    return HttpResponse ('slug list BAD REQUEST')