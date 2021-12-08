from django.urls import path
from . import views

app_name = "makedata"
urlpatterns = [
    path('movie_data/', views.movie_data),
    path('genre_data/', views.genre_data),

]