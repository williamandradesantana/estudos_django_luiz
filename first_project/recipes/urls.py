from django.urls import path
from . import views

# dominio/recipes/home
urlpatterns = [
    path('', views.home),  # Home
    path('sobre/', views.about),
    path('contato/', views.contact),
    path('recipes/<int:id>/', views.recipe)
]
