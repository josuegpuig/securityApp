from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'evaluations'

urlpatterns = [
    path('', views.EvaluationList.as_view()),
    path('<int:pk>/', views.EvaluationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)