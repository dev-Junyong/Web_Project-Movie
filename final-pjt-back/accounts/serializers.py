from rest_framework import serializers
from django.contrib.auth import get_user_model

from community.models import Review, Comment
from movies.models import Genre, Movie


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name', 'profile_photo']


class UserSerializer(serializers.ModelSerializer):
    class ReviewSerializer(serializers.ModelSerializer):
        class MovieSerializer(serializers.ModelSerializer):
            class Meta:
                model = Movie
                fields = ['id', 'title', 'poster_path', 'vote_average', 'release_date']

        class CommentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Comment
                fields = ['id']

        movie = MovieSerializer(required=False)
        review_comments = CommentSerializer(required=False, many=True)
        class Meta:
            model = Review
            fields = '__all__'

    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ['id', 'name']

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ['id', 'title', 'poster_path', 'vote_average', 'release_date']
    review_author = ReviewSerializer(required=False, many=True)
    like_genres = GenreSerializer(required=False, many=True)
    like_movies = MovieSerializer(required=False, many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'profile_photo', 'following', 'followers', 'review_author', 'is_staff', 'like_movies', 'like_genres',]
        read_only_fields = ['is_staff', 'review_author', 'following', 'followers']


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'name', 'profile_photo']


class PasswordChangeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        read_only_fields = ['email', 'username']