from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def index(request):
    return HttpResponse('VERY Главная страница')

# Страница с груповыми постами
def group_posts(request, slug):
    return HttpResponse('These are group_posts')

