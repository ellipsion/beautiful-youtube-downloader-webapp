from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name="index"),
    path('search/', views.searchView, name="search"),
    path('all-streams/', views.allStreamsView, name="all-streams"),
    path('get-all-streams/', views.getAllStreamsView, name="get-all-streams"),
]