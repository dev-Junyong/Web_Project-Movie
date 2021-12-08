from django.db import models
from django.contrib.auth.models import AbstractUser

from movies.models import Genre, Movie
from community.models import Review, Comment

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50)
    profile_photo = models.ImageField(upload_to='image', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    like_movies = models.ManyToManyField(Movie)
    like_genres = models.ManyToManyField(Genre)
    # like_reviews = models.ManyToManyField(Review, related_name='review_like_users')
    # like_comment = models.ManyToManyField(Comment, related_name='comment_like_users')

    def __str__(self):
        return self.username
