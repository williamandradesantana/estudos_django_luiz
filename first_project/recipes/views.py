from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', status=201, context={'name': 'William', 'team': 'Flamengo'})


def contact(request):
    return render(request, 'recipes//pages/contato.html', context={'contact': "(79) 99916-5932"})


def about(request):
    return render(request, 'recipes/pages/sobre.html')


def temporary(request):
    return render(request, 'index.html', status=201, context={'situation': 'temporary'})
