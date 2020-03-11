from  django.urls import path

from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter, NestedRouterMixin

from countries.views import CityViewSet
from .views import CityStatistics

app_name = 'cities'

router = routers.DefaultRouter()

router.register('', CityViewSet)
#router.register('<int:pk>/statistics', CityStatistics)

urlpatterns = [
    #path('<str:name>/',name, name='name'),
    #path('hola-mundo',index, name='index'),
    #path('<int:pk>/statistics', CityStatistics),
    #path('statistics', CityStatistics),
]

urlpatterns += router.urls