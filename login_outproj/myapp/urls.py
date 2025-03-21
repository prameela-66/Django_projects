from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),

]
