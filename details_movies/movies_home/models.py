from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_title = models.CharField(max_length=250)
    movie_description = models.TextField()
    yearof_release = models.IntegerField()
    movie_rating = models.IntegerField()
    movie_tag = models.CharField(max_length=250)
    movie_thumbnail = models.ImageField(upload_to='thumbnail')

    def __str__(self):
        return self.movie_title