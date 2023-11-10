from django.shortcuts import render
from django.http import HttpResponse as res


def home(request):
    return render(request, 'recipes/home.html')

def sobre(request):
    return res("SOBRE")

def contato(request):
    return res('CONTATO')


