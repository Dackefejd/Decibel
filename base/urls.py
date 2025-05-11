from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/', views.pages, name='home'),
]
