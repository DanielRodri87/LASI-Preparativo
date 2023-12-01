from django.urls import include, path
from recipes.views import home
from . import views 
urlpatterns = [
    path('', views.home), # Home    path('sobre/', sobre), # /sobre
    path('recipes/<int:id>/', views.recipe),
]

