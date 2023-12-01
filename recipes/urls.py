from django.urls import pathfrom recipes.views import home
from . import views # da pasta que estou importo views
urlpatterns = [
    path('', views.home), # Home    path('sobre/', sobre), # /sobre
    path('recipes/<int:id>/', views.recipe),
]

