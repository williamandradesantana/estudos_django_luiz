from django.shortcuts import render
#  HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST


def home(request):
    return render(request, 'recipes/home.html', status=201, context={
        'name': 'William',
    })
    # return HTTP Response


def contact(request):
    return render(request, 'recipes/contato.html')


def about(request):
    return render(request, 'recipes/sobre.html')
