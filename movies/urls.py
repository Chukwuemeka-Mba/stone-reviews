from django.urls import path
from .views import movie_create, MovieListView, MovieDetailView, movie_update, movie_delete, review_create

app_name = 'movies'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('create/', movie_create, name='movie-create'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
    path('<int:pk>/update', movie_update, name='movie-update'),
    path('<int:pk>/delete', movie_delete, name='movie-delete'),
    path('<int:pk>/review/', review_create, name='movie-review')
]
