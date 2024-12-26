from django.shortcuts import render
from utils.recipes import factory
from recipes.models import Recipe, Category
from django.http import Http404

def home(request):

    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', 
        status=201, 
        context={'recipes': recipes}
    )

def category(request, category_id):

    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
        ).order_by('-id')
    
    if not recipes:
        raise Http404('Not found')

    return render(request, 'recipes/pages/category.html', 
        status=201, 
        context={
            'recipes': recipes,
            'title': f'{recipes.first().category.name} - Category |'
            }
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

