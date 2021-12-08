from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('genre_list/', views.genre_list, name='genre_list'),
    path('movie_list/', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('select_genre/', views.select_genre, name='select_genre'),
    path('<int:genre_id>/genre_recommend/', views.genre_recommend, name='genre_recommend'),
    path('<int:movie_id>/movie_like/', views.movie_like, name='movie_like'),
    path('<keyword>/search_movie/', views.search_movie, name='search_movie'),
]