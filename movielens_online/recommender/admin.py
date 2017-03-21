from django.contrib import admin

# Register your models here.
from .models import Movie, Rater, Rating

admin.site.register(Movie)
admin.site.register(Rater)
admin.site.register(Rating)
