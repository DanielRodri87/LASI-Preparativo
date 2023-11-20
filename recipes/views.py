from django.shortcuts import render
from django.http import HttpResponse as res

def home(request):
    return render(request, 'recipes/pages/home.html', context={
       'name': 'Daniel',
    })
    
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
       'name': 'Daniel',
    })
