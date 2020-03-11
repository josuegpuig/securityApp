from rest_framework import serializers

#Locales
from .models import Country, State, City
from evaluations.models import Evaluation

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'short_name', 'code']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['name', 'short_name', 'code', 'country']

class CitySerializer(serializers.ModelSerializer):
    evaluations = serializers.PrimaryKeyRelatedField(many=True, queryset=Evaluation.objects.all())

    class Meta:
        model = City
        fields = ['name', 'short_name', 'code', 'state', 'evaluations']