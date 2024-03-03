from django.shortcuts import render
from .serializer import CarrosSerializer
from .models import Carros
from .serializer import MotosSerializer
from .models import Motos
from .serializer import BicisSerializer
from .models import Bicis

from rest_framework import viewsets
# Create your views here.

class CarrosViewset(viewsets.ModelViewSet):
    queryset= Carros.objects.all()
    serializer_class = CarrosSerializer
    
class MotosViewset(viewsets.ModelViewSet):
    queryset= Motos.objects.all()
    serializer_class = MotosSerializer
    
class BicisViewset(viewsets.ModelViewSet):
    queryset= Bicis.objects.all()
    serializer_class = BicisSerializer
