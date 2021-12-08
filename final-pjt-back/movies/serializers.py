from rest_framework import serializers
from .models import Genre, Movie
from community.serializers import ReviewSerializer
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(required=False, read_only=True, many=True)
    user_set = UserSerializer(required=False, read_only=True, many=True)
    genres = GenreSerializer(required=False, read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'
