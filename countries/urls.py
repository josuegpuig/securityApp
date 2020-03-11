from  django.urls import path

from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter, NestedRouterMixin

from .views import CountryViewSet, StateViewSet, CityViewSet

app_name = 'countries'

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()
country_router = router.register('', CountryViewSet, basename='country')
country_router.register('states', StateViewSet, basename="country-states",parents_query_lookups=['country']).register('cities', CityViewSet, basename='country-state-city', parents_query_lookups=['state__country', 'state'])

urlpatterns = [
    #path('<str:name>/',name, name='name'),
    #path('hola-mundo',index, name='index'),
]

urlpatterns += router.urls