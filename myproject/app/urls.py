from django.urls import path
from .views import home1,show

app_name='app'
urlpatterns=[
    path('home/',home1,name='home1'),
    path('show/',show,name='show'),
]