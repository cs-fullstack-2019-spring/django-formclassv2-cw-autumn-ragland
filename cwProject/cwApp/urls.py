from django.urls import path
from . import views

# on load take the user to the form
urlpatterns = [
    path('', views.index, name='index')
]
