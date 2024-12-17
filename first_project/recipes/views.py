from django.shortcuts import render
from utils.recipes import factory

def home(request):
    return render(request, 'recipes/pages/home.html', 
        status=201, 
        context={'recipes': [factory.make_recipe() for _ in range (10)]})


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html',
        context={
            'recipe': factory.make_recipe(),
            'is_detail_page': True
        })

def contact(request):
    return render(request, 'recipes//pages/contato.html', context={'contact': "(79) 99916-5932"})


def about(request):
    return render(request, 'recipes/pages/sobre.html')

