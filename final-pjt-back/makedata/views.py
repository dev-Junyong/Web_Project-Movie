from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from movies.models import Movie, Genre
from movies.serializers import GenreSerializer

import requests
import logging, traceback
import datetime

# Create your views here.
@api_view(['GET'])
def movie_data(request):
    link="456"

    for tmp in Movie.objects.all():
        tmp.delete()

    for page in range(1, 501):
        res = requests.get(link+str(page))
        data_lst = res.json()["results"]

        for movie_data in data_lst:
            movie_id = movie_data["id"]
            link2 = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=456&append_to_response=videos&language=ko"
            res2 = requests.get(link2)
            data = res2.json()

            title = data.get("title")
            popularity = float(data.get("popularity"))
            vote_count = int(data.get("vote_count"))
            vote_average = float(data.get("vote_average"))
            overview = data.get("overview")
            poster_path = data.get("poster_path")
            backdrop_path = data.get("backdrop_path")

            try :
                release_date = datetime.datetime.strptime(data.get("release_date"), '%Y-%m-%d')
                if not release_date :
                    continue
            except :
                continue


            movie = Movie.objects.create(
                id=movie_id,
                title = title,
                release_date = release_date,
                vote_count = vote_count,
                vote_average = vote_average,
                overview = overview,
                poster_path = poster_path,
                popularity = popularity,
                backdrop_path = backdrop_path,
            )
            for m_genre in data.get('genres'):
                genre = Genre.objects.get(pk=m_genre.get('id'))
                movie.genres.add(genre)

    return Response()



@api_view(['GET'])
def genre_data(request):
    res = requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=456&language=ko")
    data = res.json()["genres"]
    serializer = GenreSerializer(data=data, many=True)

    try:
        serializer.is_valid(raise_exception=True)
    except:
        logging.error(traceback.format_exc())

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

