from django.db import models
from django.conf import settings

from movies.models import Movie

# Create your models here.
# class MovieCup(models.Model):
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='moviecup')
#     movies = models.ManyToManyField(Movie, related_name='moviecups')
    
#     created_at = models.DateTimeField



class MovieCupMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # moviecup = models.ForeignKey(MovieCup, on_delete=models.CASCADE)


# class Top

