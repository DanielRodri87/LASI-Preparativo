from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), # O include serve para que as urls do app sejam chamadas para a parte principal do projeto


]

