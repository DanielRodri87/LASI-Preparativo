from django.contrib import admin
from django.urls import path
from django.http import HttpResponse as res # Aqui chamo uma função genéria para retornar, porque toda view prencisa gerar um Request e retornar um responde
# função temporária:


#HTTP Request 
def my_view(request):
    return res('o inicio de um sonho')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', my_view),
]

