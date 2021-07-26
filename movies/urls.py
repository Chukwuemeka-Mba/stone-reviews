from django.urls import path
from .views import MovieCreateView, MovieListView, MovieUpdateView, MovieDeleteView, ReviewCreateView, movie_detail

app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('create/', MovieCreateView.as_view(), name='movie-create'),
    path('<int:pk>', movie_detail, name='movie-detail'),
    path('<int:pk>/update', MovieUpdateView.as_view(), name='movie-update'),
    path('<int:pk>/delete', MovieDeleteView.as_view(), name='movie-delete'),
    path('<int:pk>/review/', ReviewCreateView.as_view(), name='movie-review')
]
