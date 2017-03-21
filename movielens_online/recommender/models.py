from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    imdb = models.CharField(max_length=200)
    release_date = models.CharField(max_length=20)
    video_release = models.CharField(max_length=20)

    def __repr__(self):
        return "{}: {}".format(self.id, self.title)

    def __str__(self):
        return self.__repr__()


class Rater(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    zipcode = models.IntegerField()

    def __repr__(self):
        return "{}: {}".format(self.id, self.name)

    def __str__(self):
        return self.__repr__()


class Rating(models.Model):

    rater = models.ForeignKey('Rater', on_delete=models.CASCADE,)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE,)
    rating = models.IntegerField()
    timstamp = models.IntegerField()

    def __repr__(self):
        return "{}".format(self.title)

    def __str__(self):
        return self.__repr__()
