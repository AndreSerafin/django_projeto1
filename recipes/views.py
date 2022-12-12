from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'andre pereira',
        'age': 22,
        'height': 1.70,
    })
