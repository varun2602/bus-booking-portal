from django.shortcuts import render, HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from . import models 
import requests 
from django.conf import settings
import json
import io

class UserRegistrationView(generics.ListCreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = models.CustomUser.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class SearchBusesView(APIView):
   
    def get(self, request, *args, **kwargs):
        # Define the URL and the Bearer token
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        source = python_data.get("source", None)
        destination = python_data.get("destination", None)
        if not source or not destination:
             return HttpResponse(json.dumps({"error": "source and destination are required"}),content_type="application/json",status=400)
        search_bus_url = settings.SEARCH_BUS
        auth_header = request.headers.get('Authorization', None)
        token = None
        if auth_header and auth_header.startswith('Bearer '):
            # Extract the token part of the header
            token = auth_header.split(' ')[1]

        if not token:
            return HttpResponse(json.dumps({"error": "Please login"}),content_type="application/json",status=403)
        

        # Define the parameters
        params = {
            "source": source,
            "destination": destination
        }

        # Define the headers
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        # Perform the GET request
        response = requests.get(search_bus_url, headers=headers, json=params)
        return HttpResponse(response, content_type="application/json",status=200)

class BlockSeatsView(APIView):
  
    def post(self, request, *args, **kwargs):
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        bus_name = python_data.get("bus_name", None)
        no_passengers = python_data.get("no_passengers", None)
        if not bus_name or not no_passengers:
            return HttpResponse(json.dumps({"error": "bus name and number of passengers required"}),content_type="application/json",status=400)
        block_url = settings.BLOCK_URL
        auth_header = request.headers.get('Authorization', None)
        token = None
        if auth_header and auth_header.startswith('Bearer '):
            # Extract the token part of the header
            token = auth_header.split(' ')[1]

        if not token:
           return HttpResponse(json.dumps({"error": "Please login"}),content_type="application/json",status=403)
        params = {
            "bus_name":bus_name,
            "no_passengers":no_passengers
            }
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.post(block_url, headers=headers, json=params)
        return HttpResponse(response, content_type="application/json",status=200)
        

class BookTicketsView(APIView):
    
    def post(self, request, *args, **kwargs):
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        block_id = python_data.get("block_id", None)
        
        if not block_id:
            return HttpResponse(json.dumps({"error": "block_id"}),content_type="application/json",status=400)
        book_url = settings.BOOK_URL
        auth_header = request.headers.get('Authorization', None)
        token = None
        if auth_header and auth_header.startswith('Bearer '):
            # Extract the token part of the header
            token = auth_header.split(' ')[1]

        if not token:
           return HttpResponse(json.dumps({"error": "Please login"}),content_type="application/json",status=403)
        params = {
            "block_id": block_id
            }
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.post(book_url, headers=headers, json=params)
        return HttpResponse(response, content_type="application/json",status=200)

