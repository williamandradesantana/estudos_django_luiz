from django.shortcuts import render
from django.http import HttpResponse

#  HTTP REQUEST <- HTTP RESPONSE

# HTTP REQUEST


def home(request):
    return render(request, 'recipes/home.html', status=201, context={
        'name': 'William',
    })
    # return HTTP Response


def about(request):
    return render(request, 'temp/temp.html')


def contact(request):
    return HttpResponse('Contact')
