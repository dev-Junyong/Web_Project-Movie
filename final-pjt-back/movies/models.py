from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    # genre_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    release_date = models.CharField(max_length=100, null=True)
    popularity = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    vote_average = models.FloatField(null=True)
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=500, null=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    adult = models.BooleanField(null=True)
    backdrop_path = models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.title


class CREDIT(models.Model):
    pass
