from django.shortcuts import render, get_object_or_404
from .models import Movie, Rater  #, Rating
from django.db.models import Count, Avg


# Create your views here.
def index(request):
    # TODO: User welcome <Logged in user> and links to other pages
    my_profile = Rater.objects.all()
    return render(request, 'recommender/index.html', {'my_profile': my_profile})


def top_20(request):
    top20 = Movie.objects.annotate(avg=Avg('rating'), rate_count=Count('rating')).order_by('-rate_count', 'avg')[:20]
    return render(request, 'recommender/top_20.html', {'top20': top20})


def movie_list(request):
    movies = [movies for movies in Movie.objects.all()]
    return render(request, 'recommender/movie_list.html', {'movies': movies})


def rater_list(request):
    users = [rater for rater in Rater.objects.all()]
    return render(request, 'recommender/rater_list.html', {'users': users})


def movie_profile(request, movie_id):
    m = get_object_or_404(Movie, pk=movie_id)
    avg_rating = m.rating_set.aggregate(Avg('rating'))['rating__avg']
    rating_count = m.rating_set.aggregate(Count('rating'))['rating__count']
    all_movie_rating = m.rating_set.all().order_by('timstamp')
    return render(request, 'recommender/movie_profile.html', {'m': m, 'avg_rating': round(avg_rating, 2), 'rating_count': rating_count, 'all_movie_rating': all_movie_rating})


def rater_profile(request, rater_id):
    r = get_object_or_404(Rater, pk=rater_id)
    movies_reviewed = r.rating_set.aggregate(Count('rating'))['rating__count']
    top10 = r.rating_set.order_by('-rating', 'timstamp')
    return render(request, 'recommender/rater_profile.html', {'r': r, 'movies_reviewed': movies_reviewed, 'top10': top10})
