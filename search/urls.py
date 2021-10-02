from django.contrib import admin
from django.urls import path
from search import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_search/', views.new_search, name='new_search')
]
