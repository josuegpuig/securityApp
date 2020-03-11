from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import NestedViewSetMixin

from .models import Country, State, City
from .serializers import CountrySerializer, StateSerializer, CitySerializer

# Create your views here.
class CountryViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    #permission_classes = (IsAuthenticated,)

    queryset = City.objects.all()
    serializer_class = CitySerializer