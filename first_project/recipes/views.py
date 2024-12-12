from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', status=201, context={
        'name': 'William',
    })
    # return HTTP Response


def contact(request):
    return render(request, 'recipes/contato.html', context={'contact': "(79) 99916-5932"})


def about(request):
    return render(request, 'recipes/sobre.html')
