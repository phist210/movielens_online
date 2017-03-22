from django.http import HttpResponse
from models import Movie


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def top_20(request):
    movies = [movies for movies in Movie.object.all()]
    return render(request, 'recommender/top_20.html', {'question': })
