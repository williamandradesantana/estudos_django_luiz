from django.urls import path
from recipes.views import home, about, contact

# dominio/recipes/home
urlpatterns = [
    path('', home),  # Home
    path('sobre/', about),
    path('contato/', contact)
]
