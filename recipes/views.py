from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'andre pereira',
        'age': 22,
        'height': 1.70,
    })


def contato(request):
    return HttpResponse('Sobre')


def sobre(request):
    return render(request, 'recipes/sobre.html')
