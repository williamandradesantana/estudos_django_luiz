from django.shortcuts import render
from utils.recipes import factory
from recipes.models import Recipe, Category

def home(request):

    recipes = Recipe.objects.all().order_by('-id')

    return render(request, 'recipes/pages/home.html', 
        status=201, 
        context={'recipes': recipes }
    )

def category(request, category_id):

    recipes = Recipe.objects.filter(
        category__id=category_id).order_by('-id')
    
    return render(request, 'recipes/pages/home.html', 
        status=201, 
        context={'recipes': recipes }
    )

def recipe(request, id):

    recipe = Recipe.objects.filter(id=id).first()

    return render(request, 'recipes/pages/recipe-view.html',
        context={
            'recipe': recipe,
            'is_detail_page': True
        })

def contact(request):
    return render(request, 'recipes//pages/contato.html', context={'contact': "(79) 99916-5932"})


def about(request):
    return render(request, 'recipes/pages/sobre.html')

