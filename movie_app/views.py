from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Afisha.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from .models import Movie, Director, Review
from django.db.models import Avg, Count


@api_view(['GET'])
def movie_item_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie, many=False).data
    if request.method == 'GET':
        serializer = MovieSerializer()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(data=data)


@api_view(['GET'])
def movie_list_api_view(request):
    movies = Movie.objects.all()
    data = MovieSerializer(instance=movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def director_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'Director not found!'},
                         status=status.HTTP_404_NOT_FOUND)
    data = DirectorSerializer(director, many=False).data
    if request.method == 'GET':
        serializer = DirectorSerializer()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(data=data)


@api_view(['GET'])
def director_list_api_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        movies_count = Director.objects.aggregate(count_movies=Count('director'))
        data_dict = DirectorSerializer(director, many=True).data
        return Response(data=[data_dict, movies_count])


@api_view(['GET'])
def movie_api_view(request):
    dict_ = {
        'text': 'Hello World!',
        'int': 1000,
        'bool': True,
        'float': 2.99,
        'list': [1, 2, "different"],
        'dict': {
            'text': 'hello'
        }
    }

    return Response(data=dict_)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(instance=reviews, many=True).data

    return Response(data=data)


@api_view(['GET'])
def review_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewSerializer(review, many=True).data
    if request.method == 'GET':
        serializer = ReviewSerializer()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(data=data)



