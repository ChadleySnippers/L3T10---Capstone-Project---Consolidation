from django.urls import path
from . import views

# Define a URL pattern for the default view, mapping the empty path to the 'index' view
urlpatterns = [
    path('', views.index, name='index')
]
