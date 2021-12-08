from rest_framework import serializers

from .models import Review, Comment
from movies.models import Movie

from accounts.serializers import UserSerializer

# Review Create
class ReviewSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    author = UserSerializer(required=False)
    movie= MovieSerializer(required=False)

    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'author', 'rank', 'created_at', 'updated_at', 'movie', 'users_like')
        read_only_fields = ('id', 'author', 'created_at', 'updated_at', 'movie', 'users_like')


# List
class ReviewListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.name")
    class Meta:
        model = Review
        fields = ('id', 'title', 'author',)



#comment
class CommentSerializer(serializers.ModelSerializer):
    updated_at = serializers.DateTimeField(required=False, format="%Y-%m-%d")
    author = serializers.CharField(required=False, source="author.username")
    review = ReviewSerializer(required=False)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'like_users', 'created_at')
