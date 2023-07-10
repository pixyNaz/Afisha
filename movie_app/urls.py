from movie_app import views
from django.urls import path

urlpatterns = [
    path('movies/', views.MovieListCreateAPIView.as_view()),
    path('movies/<int:id>/', views.MoviesDetailAPIView.as_view()),
    path('directors/', views.DirectorListCreateAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
]