from django.shortcuts import render

from countries.models import City

from rest_framework.decorators import api_view
from django.http import JsonResponse
# Create your views here.

@api_view(['POST'])
def CityStatistics(request):
    selection = request.data['selection']
    #gender
    cities = City.objects.all()
    response = {}

    if selection == 'security':
        for city in cities:
            evaluations = city.evaluations.all()
            total_evaluations = len(evaluations)
            positive = 0
            for evaluation in evaluations:
                if evaluation.classification == 'pos':
                    positive += 1
                elif evaluation.classification == 'neu' and evaluation.sentiment == 'positive':
                    positive += 1
                    
            calculation = 0 if total_evaluations == 0 else (positive / total_evaluations) * 100
            response[city.name] = calculation

        return JsonResponse({
            'calculation': response
        })
    elif selection == 'insecurity':
        for city in cities:
            evaluations = city.evaluations.all()
            total_evaluations = len(evaluations)
            negative = 0
            for evaluation in evaluations:
                if evaluation.classification == 'neg':
                    negative += 1
                elif evaluation.classification == 'neu' and evaluation.sentiment == 'negative':
                    negative += 1
                    
            calculation = 0 if total_evaluations == 0 else (negative / total_evaluations) * 100
            response[city.name] = calculation

        return JsonResponse({
            'calculation': response
        })
    
    return JsonResponse({
        'message': 'Make a selection'
    })
