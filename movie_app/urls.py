from movie_app import views
from django.urls import path

urlpatterns = [
    path('', views.movie_list_api_view),
    path('directors/', views.director_list_api_view),
    path('reviews/', views.review_list_api_view),
    path('movies/<int:id>/', views.movie_item_api_view),
]