from django.urls import path
from . import views

# authors:...
app_name = 'authors'

urlpatterns = [
    path("register/", views.register_view, name="register"),
]