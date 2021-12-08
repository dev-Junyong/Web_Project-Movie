from django.contrib.auth import get_user_model
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_safe

from movies.models import Genre, Movie
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

from movies.serializers import GenreSerializer, MovieSerializer

User = get_user_model()


@api_view(['GET'])
def movie_list(request):
    latest_movies = Movie.objects.order_by('-release_date').filter(vote_count__gt=50)
    paginator = Paginator(latest_movies, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    serializer = MovieSerializer(page_obj, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def select_genre(request):
    genre_ids = request.data

    temp = []
    for genre_id in genre_ids:
        genre = get_object_or_404(Genre, pk=genre_id)
        movies = genre.movies.all()
        if not temp:
            temp.extend(movies)
        else:
            new_temp = []
            for i in temp:
                for j in movies:
                    if i == j:
                        new_temp.append(i)
            temp = new_temp
    
    paginator = Paginator(temp, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    serializer = MovieSerializer(page_obj, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user

    if user.like_movies.filter(pk=movie_id).exists():
        user.like_movies.remove(movie)
        is_like = False
    else:
        user.like_movies.add(movie)
        is_like = True

    context = {
        'is_like': is_like,
    }
    return JsonResponse(context)


@api_view(['GET'])
def search_movie(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword).order_by('-vote_count').all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_recommend(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = random.sample(list(genre.movies.all()[:60]), 16)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
