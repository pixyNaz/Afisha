from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


STAR_CHOICES = (
    (1, '*'),
    (2, 2 * '*'),
    (3, 3 * '*'),
    (4, 4 * '*'),
    (5, 5 * '*'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    # review = models.ManyToManyField(Review)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director')

    def __str__(self):
        return self.title

    @property
    def director_name(self):
        return self.director.name if self.director else 'No director'

    @property
    def review_movie(self):
        return [review.movie for review in self.reviews.all()]

    @property
    def reviews(self):
        return self.reviews_movie.filter(stars__in=[2,4])


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews_movie')
    stars = models.IntegerField(default=5, choices=STAR_CHOICES)

    def __str__(self):
        return self.text

    def __float__(self):
        return self.stars







