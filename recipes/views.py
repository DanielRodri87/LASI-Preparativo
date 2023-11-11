from django.shortcuts import render
from django.http import HttpResponse as res


def home(request):
    return render(request, 'recipes/pages/home.html', context={
       'name': 'Daniel',
    })

