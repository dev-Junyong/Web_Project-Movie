from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import random
from algo.serializers import LotteryMovieSerializer
from movies.models import Movie, Genre
from movies.serializers import GenreSerializer, MovieSerializer

from rest_framework import status

User = get_user_model()


@api_view(['GET'])
def moviecup_list(request):
    if request.user.is_authenticated:
    
        movie_list = random.sample(list(Movie.objects.order_by('-vote_count')[:200]), 32)
        serializer = MovieSerializer(movie_list, many=True)
        
        return Response(serializer.data)


@api_view(['POST'])
def winner(request):
    genres = request.data.get('genres')
    genre = genres[0]
    genre = get_object_or_404(Genre, pk=genre['id'])
    user = get_object_or_404(User, pk=request.user.id)

    if user.like_genres.filter(pk=genre.id).exists():
        pass
    else:
        user.like_genres.add(genre)

    context = {
        'msg': '성공',
    }
    return JsonResponse(context)


@api_view(['GET'])
@permission_classes([AllowAny])
def lottery(request):
    if request.user.is_authenticated:
        if request.user.like_genres.count():
            genres = GenreSerializer(request.user.like_genres, many=True)

            genre = random.sample(genres.data, 1)
            genre = get_object_or_404(Genre, pk=genre[0]['id'])
            movies = genre.movies.all()
            serializer = LotteryMovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    movie = random.sample(get_list_or_404(Movie), 1)
    serializer = MovieSerializer(movie[0])

    return Response(serializer.data, status=status.HTTP_200_OK)
