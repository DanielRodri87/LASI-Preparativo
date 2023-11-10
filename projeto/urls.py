from django.contrib import admin
from django.urls import path
from django.http import HttpResponse as res # Aqui chamo uma função genéria para retornar, porque toda view prencisa gerar um Request e retornar um responde
# função temporária:


#HTTP Request 
def home(request):
    return res('HOME')

def sobre(request):
    return res("SOBRE")

def contato(request):
    return res('CONTATO')



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', home), # Home
    path('sobre/', sobre), # /sobre
    path('contato/', contato), # Contato

]

