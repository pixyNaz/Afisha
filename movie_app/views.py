from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from Afisha.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieValidateSerializer
from .models import Movie, Director, Review
from django.db.models import Avg, Count


@api_view(['GET', 'PUT', 'DELETE'])
def movie_item_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = MovieSerializer(movie, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        return Response(data={'movie': MovieSerializer(movie).data})
    else:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    serializer = MovieValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    if request.method == 'GET':
        movies = Movie.objects.all()
        data = MovieSerializer(instance=movies, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data=serializer.errors)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')

        movie = Movie.objects.create(
            title=title, description=description, duration=duration,
            director_id=director_id
        )

        return Response(data={'movie': MovieSerializer(movie).data})


@api_view(['GET', 'PUT', 'DELETE'])
def director_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'Director not found!'},
                         status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = DirectorSerializer(director, many=False).data
        return Response(data=data)
    elif request.method == "PUT":
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director.name = request.data.get('name')
        return Response(data={DirectorSerializer(director).data})


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        director = Director.objects.all()
        movies_count = Director.objects.aggregate(count_movies=Count('director'))
        data_dict = DirectorSerializer(director, many=True).data
        return Response(data=[data_dict, movies_count])
    elif request.method == 'POST':
        name = request.data.get('name')

        director = Director.objects.create(
                name=name
         )
        return Response(data={'director': DirectorSerializer(director).data})


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


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(instance=reviews, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        review = request.data.get('review')
        review = Review.objects.create(
            review=review
        )
        return Response(data={'review': ReviewSerializer(review).data})


@api_view(['GET'])
def review_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'Review not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = request.data.get('text')
        review.movie = request.data.get('movie')
        review.stars = request.data.get('stars')
        return Response(data={'review': ReviewSerializer(review).data})
    else:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




