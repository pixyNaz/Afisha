from rest_framework import serializers
from select import select

from movie_app.models import Movie, Director, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id description director reviews'.split()

