
from .models import Bathroom, Review
from rest_framework import serializers

class BathroomSerialization(serializers.ModelSerializer):
    class Meta:
        model = Bathroom
        fields = ['id', 'name']

class ReviewSerialization(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'pub_date', 'user_name', 'comment', 'rating']
