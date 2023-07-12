from rest_framework import serializers
from .models import Bread


class Breadserializer(serializers.ModelSerializer):
    class Meta:
        model = Bread
        fields = [
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'sheddingamount',
            'exerciseneeds',
        ]
