from django.urls import path
from . import views

# recipes:home
app_name = 'recipes'

# dominio/recipes/home
urlpatterns = [
    path('', views.home, name='home'),  # Home
    path('sobre/', views.about),
    path('contato/', views.contact),
    path('recipes/<int:id>/', views.recipe, name='recipe')
]
