from rest_framework import serializers

from movie_app.models import Movie, Director, Review
from rest_framework.exceptions import ValidationError


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
        fields = 'id title description director reviews'.split()


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=100)
    description = serializers.CharField(min_length=2, max_length=500)
    duration = serializers.FloatField(min_value=0.5, max_value=4)
    director_id = serializers.CharField(min_length=1, max_length=100)

    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('Director not found!')
        return director_id

    def validate_reviews(self, reviews):
        reviews_obs = Review.objects.filter(id__in=reviews)
        if len(reviews) != len(reviews_obs):
            raise ValidationError('Review not found!')
        return reviews

    def validate_movie(self, movies):
        movies_obj = Movie.objects.filter(id__in=movies)
        if len(movies) != len(movies_obj):
            raise ValidationError('Movie not found!')
