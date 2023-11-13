from django.shortcuts import render
from .serializers import LocationSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location

import requests

def get_weather_data(latitude,longitude):
    grid_url = f"https://api.weather.gov/points/{latitude},{longitude}/forecast"
    grid_response = requests.get(grid_url)
    grid_data = grid_response.json()
    grid_id = grid_data['properties']['gridId']
    grid_x = grid_data['properties']['gridX']
    grid_y = grid_data['properties']['gridY']
    url = grid_data['properties']['forecast']
    # url = f"https://api.weather.gov/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast"
    response = requests.get(url)
    data = response.json()
    temperature = data['properties']['periods'][0]['temperature']
    humidity = data['properties']['periods'][0]['relativeHumidity']['value']
    return temperature,humidity

class GeoLocationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class GeoLocationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class GeolocationWeatherAPIView(APIView):
    def get(self,request,pk):
        location = Location.objects.get(pk=pk)
        temperature, humidity = get_weather_data(location.location.y,location.location.x)
        data = {
            'id':location.id,
            'name': location.name,
            'location':location.location,
            'temperature':temperature,
            'humidity':humidity 
        }
        return Response(data)

