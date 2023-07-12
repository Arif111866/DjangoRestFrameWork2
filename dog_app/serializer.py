from rest_framework import serializers
from .models import Bread
from .models import Dog

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
class Dogserializer(serializers.ModelSerializer):
    bread = serializers.SlugRelatedField(slug_field ="name" , queryset=Bread.objects.all())
    class Meta:
        model = Dog
        fields = [
            'id',
            'name', 
            'age' ,
            'bread', 
            'gender',  
            'color' ,
            'favoritefood',  
            'favoritetoy',
        ]
