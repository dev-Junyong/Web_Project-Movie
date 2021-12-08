from django.db import models
from django.conf import settings

from movies.models import Movie
User = settings.AUTH_USER_MODEL

# Create your models here.
class Review(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_author')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_reviews")
    
    users_like = models.ManyToManyField(User, related_name='review_like', blank=True)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    rank = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')
    
    like_users = models.ManyToManyField(User, related_name='comment_like')
    
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
