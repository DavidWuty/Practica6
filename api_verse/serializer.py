from rest_framework import serializers
from .models import Carros
from .models import Motos
from .models import Bicis

class CarrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carros
        fields = '__all__'
        
class MotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motos
        fields = '__all__'
        
class BicisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicis
        fields = '__all__'
        
