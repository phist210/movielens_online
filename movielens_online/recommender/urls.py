from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin


app_name = 'recommender'

urlpatterns = [
    url(r'^$', views.index, name='recommender'),
    url(r'^top_20/$', views.top_20, name='top_20'),
    url(r'^movie_list/$', views.movie_list, name='movie_list'),
    url(r'^movie_list/(?P<movie_id>[0-9]+)/', views.movie_profile, name='movie_profile'),
    url(r'^rater_list/$', views.rater_list, name='rater_list'),
    url(r'^rater_list/(?P<rater_id>[0-9]+)/', views.rater_profile, name='rater_profile'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    ]
