from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', status=201, context={'name': 'William', 'team': 'Flamengo'})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html',)

def contact(request):
    return render(request, 'recipes//pages/contato.html', context={'contact': "(79) 99916-5932"})


def about(request):
    return render(request, 'recipes/pages/sobre.html')

