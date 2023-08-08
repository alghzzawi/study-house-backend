from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .jwt_tokens import MyTokenObtainPairView
from .views import registration_view,UserViewSet
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', registration_view, name="register"),
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('users/<str:username>', UserViewSet.as_view({'get': 'retrieve'})),
]