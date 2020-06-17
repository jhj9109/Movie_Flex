from rest_framework import serializers
from .models import Movie

class MovieCarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'poster_path')