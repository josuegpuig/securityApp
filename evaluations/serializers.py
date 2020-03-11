from rest_framework import serializers
from .models import Evaluation

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        user = serializers.ReadOnlyField(source='user.username')
        fields = ['id', 'opinion', 'user', 'city', 'sentiment', 'classification']