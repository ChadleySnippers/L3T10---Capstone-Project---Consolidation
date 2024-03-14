"""
URL configuration for pollProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# Import necessary modules
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Define URL patterns for the Django project
urlpatterns = [
    # Set the default URL to the login view using Django's built-in LoginView
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # Include Django's built-in authentication URLs for handling login, logout, etc.
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Admin site URL
    path("admin/", admin.site.urls),
    
    # Include URLs from the 'landingPage' app under the path 'polls'
    path("polls", include('landingPage.urls')),
    
    # Include URLs from the 'pollApp' app under the path 'polls/'
    path("polls/", include('pollApp.urls')),
    
    # Include additional Django's built-in authentication URLs under the path 'accounts/'
    path("accounts/", include('django.contrib.auth.urls')),
]
