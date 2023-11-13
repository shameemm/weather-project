from django.urls import path 
from .views import GeoLocationListCreateAPIView,GeoLocationRetrieveUpdateDestroyAPIView,GeolocationWeatherAPIView

urlpatterns = [
    path('locations/', GeoLocationListCreateAPIView.as_view(),name='location-list-create'),
    path('locations/<int:pk>/', GeoLocationRetrieveUpdateDestroyAPIView.as_view(), name='location-detail'),
    path('locations/<int:pk>/weather/', GeolocationWeatherAPIView.as_view(), name='location-weather'),
]
