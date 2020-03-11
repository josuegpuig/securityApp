from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet
from rest_framework_simplejwt import views as jwt_views

app_name = 'accounts'

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]