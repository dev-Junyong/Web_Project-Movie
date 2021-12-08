from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import GenreSerializer

from movies.models import Movie

User = get_user_model()

class WinnerMovieSerializer(serializers.ModelSerializer):

    like_genres = GenreSerializer(required=False, many=True)
    class Meta:
        model = User
        fields = ('like_genres', )


class LotteryMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path',)
