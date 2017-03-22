from django.conf.urls import url
from . import views

app_name = 'recommender'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^top_20/$', views.top_20, name='top_20'),
    url(r'^movie_list/$', views.movie_list, name='movie_list'),
    url(r'^movie_list/(?P<movie_id>[0-9]+)/', views.movie_profile, name='movie_profile'),
    url(r'^rater_list/$', views.rater_list, name='rater_list'),
    url(r'^rater_list/(?P<rater_id>[0-9]+)/', views.rater_profile, name='rater_profile'),

]
