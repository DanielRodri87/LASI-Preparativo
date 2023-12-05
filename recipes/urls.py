from django.urls import include, path
from recipes.views import home
from . import views 

# recipes:recipe --> eu uso dois pontos no html
app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]

